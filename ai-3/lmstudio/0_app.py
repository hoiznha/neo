#로컬에서 실행중인 LM stduio 서버에 요청을 보내서 llama3.2을 사용하여 대화형 응답을 생성하는 예제입니다.
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:1234/v1")

model_name = "llama3.2"

try:
    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {'role' : 'system', 'content':'You are a helpful assistant.'}, #system 메세지는 AI의 성격정의
            {'role' : 'user', 'content' : 'What is the meaning of life?'} #user 메세지는 사용자의 질문
        ],
        max_tokens=300,
        temperature=0.7,
    )

    print(completion.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
    print('Plase check the LM Studio server is running, accessible at the specified url, and a model is loaded.')

