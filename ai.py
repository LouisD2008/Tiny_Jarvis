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
        yield chunk.message.content
