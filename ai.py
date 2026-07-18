from llama_cpp import Llama


llm = Llama(
    model_path="./models/model-Q4_K_M.gguf",
    n_ctx = 2048,
    n_threads = 4,  # cos rpi5 processor has 4 cores
    flash_attn = True,  # optimizes the math heavy lifting
)


def generate(prompt):
    response = llm.create_chat_completion(
        messages=[{
            'role': 'user',
            'content': "Answer in a concise, thoughtful way to the following prompt: " + prompt
        }],
        stream = True,
        cache_prompt = True   # avoids recalculating the whole history on every turn
    )
    for chunk in response:
        delta = chunk['choices'][0]['delta']
        if 'content' in delta:
            yield delta['content']


def sentence_buffer(token_gen):
    buffer = ""
    sentence_endings = {'.', '?', '!', '\n', ';', ':'}
    for token in token_gen:
        buffer += token
        if any(buffer.strip().endswith(ending) for ending in sentence_endings):  # "any" keyword returns True if any item in an iterable is True, so here if any buffer element ends with one of the elements in sentence_endings
            yield buffer.strip()
            buffer = ""
    if buffer.strip():
        yield buffer.strip()