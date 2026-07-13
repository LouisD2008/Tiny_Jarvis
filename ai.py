# Prequesites: ollama running, and model pulled (ollama pull <model>)
from ollama import chat
from ollama import ChatResponse


def generate(prompt):
    response: ChatResponse = chat(model='gemma3', messages=[
        {
        'role': 'user',
        'content': "Answer in a concise, thoughtful way to the following prompt: " + prompt
        # stream = true
        },
    ])
    return response.message.content
