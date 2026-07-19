#!/bin/bash
set -e

echo "=========================================="
echo "  Tiny Jarvis Installer"
echo "=========================================="

# Check if running on Raspberry Pi
if ! grep -q "Raspberry Pi" /proc/cpuinfo 2>/dev/null; then
    echo "WARNING: This doesn't appear to be a Raspberry Pi."
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""
echo "[1/9] Installing system dependencies..."
sudo apt update
sudo apt install -y \
    git \
    python3 \
    python3-venv \
    python3-dev \
    python3-pip \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff6-dev \
    libportaudio2 \
    portaudio19-dev \
    cmake \
    build-essential \
    wget \
    librespot

echo ""
echo "[2/9] Checking GPU memory allocation..."
GPU_MEM=$(vcgencmd get_mem gpu | cut -d= -f2 | cut -dM -f1)
if [ "$GPU_MEM" -gt 16 ]; then
    echo "WARNING: GPU memory is ${GPU_MEM}M. For best performance, set gpu_mem=16 in /boot/firmware/config.txt"
    echo "Current setting: $(vcgencmd get_mem gpu)"
fi

echo ""
echo "[3/9] Enabling I2C interface..."
if ! grep -q "^dtparam=i2c_arm=on" /boot/firmware/config.txt 2>/dev/null; then
    echo "dtparam=i2c_arm=on" | sudo tee -a /boot/firmware/config.txt > /dev/null
    echo "I2C enabled in config.txt. Reboot required for full effect."
else
    echo "I2C already enabled."
fi
sudo modprobe i2c-dev 2>/dev/null || true

echo ""
echo "[4/9] Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo ""
echo "[5/9] Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "[6/9] Installing llama-cpp-python with ARM optimizations..."
echo "This will take 10-30 minutes. Grab a coffee."
CMAKE_ARGS="-DLLAMA_NATIVE=ON -DLLAMA_ARM_ARCH=armv8.4-a" \
    pip install llama-cpp-python --no-cache-dir

echo ""
echo "[7/9] Setting up performance mode..."
sudo tee /etc/systemd/system/cpu-performance.service > /dev/null << 'EOF'
[Unit]
Description=Set CPU governor to performance
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/bin/bash -c 'echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor'
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now cpu-performance

echo ""
echo "[8/9] Creating necessary directories..."
mkdir -p models piper_voices recordings

echo ""
echo "[9/9] Downloading AI model and Piper voice..."

echo "  -> Downloading Llama 3.2 3B (Q4_K_M) ~2GB..."
wget -q --show-progress -P models/ \
    https://huggingface.co/osmapi/Nidum-Llama-3.2-3B-Uncensored-GGUF/resolve/main/model-Q4_K_M.gguf \
    || echo "WARNING: Model download failed. Download manually from: https://huggingface.co/osmapi/Nidum-Llama-3.2-3B-Uncensored-GGUF"

echo "  -> Downloading Piper voice..."
python -m piper.download_voices en_US-lessac-medium \
    || echo "WARNING: Piper voice download failed. Run manually: python -m piper.download_voices en_US-lessac-medium"

echo ""
echo "=========================================="
echo "  Installation complete!"
echo "=========================================="
echo ""
echo "Activate the virtual environment:"
echo "  source .venv/bin/activate"
echo ""
echo "Run Tiny Jarvis:"
echo "  python main.py"
echo ""
echo "If I2C was just enabled, reboot first:"
echo "  sudo reboot"