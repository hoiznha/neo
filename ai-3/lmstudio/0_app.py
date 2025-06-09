from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:1234/v1")

model_name = "llama3.2"

try:
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {'role' : 'system', 'content':'You are a helpful assistant.'},
            {'role' : 'user', 'content' : 'What is the meaning of life?'}
        ],
        max_tokens=300,
        temperature=0.7,
    )

    print(completion.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
    print('Plase check the LM Studio server is running, accessible at the specified url, and a model is loaded.')

