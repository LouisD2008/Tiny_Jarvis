# Prequesites: ollama running, and model pulled (ollama pull <model>)
from ollama import chat
from ollama import ChatResponse


def generate(prompt):
    response: ChatResponse = chat(
        model='gemma3', 
        messages=[{
        'role': 'user',
        'content': "Answer in a concise, thoughtful way to the following prompt: " + prompt
        }],
        stream = True
    )
    # return response.message.content
    # instead of that, we use yield keyword
    for chunk in response:
        yield chunk['message']['content']


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