#!/bin/bash
set -e

echo "Installing system dependencies..."
sudo apt update
sudo apt install -y git python3 python3-venv python3-dev \
    libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev \
    libopenjp2-7-dev libtiff6-dev libportaudio2 portaudio19-dev \
    cmake build-essential

echo "Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing Python packages..."
pip install -r requirements.txt

echo "Installing llama-cpp-python with ARM optimizations..."
CMAKE_ARGS="-DLLAMA_NATIVE=ON -DLLAMA_ARM_ARCH=armv8.4-a" \
    pip install llama-cpp-python --no-cache-dir

echo "Done. Activate with: source .venv/bin/activate"