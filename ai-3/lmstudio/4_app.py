import lmstudio as lms

model = lms.llm()

response = model.respond(
    'What is LM Studio',
    # 모델이 응답을 생성하기 위해 준비 중일때 진행률을 알려주는 콜백 함수
    on_prompt_processing_progress = (lambda progress: print(f'{progress * 100}% complete')),
)

print(response)
