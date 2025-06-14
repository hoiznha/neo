# from openai import OpenAI

# client = OpenAI(
#     base_url = "http://localhost:11434/v1",
#     api_key = "ollama",
# )

# response = client.chat.completions.create(
#     model = "llama3.2:latest",
#     messages = [
#         {'role':'system', 'content':'You are a python expert.'},
#         {'role':'user', 'content':'Code a Python function to generate a Fibonnacci sequence '}
#     ]
# )

# result = response.choices[0].message.content
# print(result)

## 2_app.py

from openai import OpenAI

client = OpenAI(
    base_url = 'http://192.168.1.3:11434/v1',
    api_key='ollama',
)

response = client.chat.completions.create(
    model = 'llama3.2:latest',
    messages = [
        {'role': 'system', 'content': 'You are a python expert. '},
        {'role': 'user', 'content': 'Code a Python function to generate a Fibonacci sequence.'}
    ]
)

result = response.choices[0].message.content
print(result) 
