import lmstudio as lms

model = lms.llm()
# chat 객체 생성. 대화 히스토리 관리
chat = lms.Chat("You are a task focused AI assistant.")

while True:
    try:
        user_input = input("You : (leave blank to exit) ")
    except EOFError:
        print()
        break
    if not user_input:
        break

    # 사용자 입력을 대화에 추가
    chat.add_user_message(user_input)
    # 대화 히스토리를 보내서 스트리밍 방식으로 받음.
    prediction_steram = model.respond_stream(
        chat,
        on_message = chat.append,
    )

    print("AI : ", end='', flush=True)

    # 스트리밍된 응답을 출력
    for fragment in prediction_steram:
        print(fragment.content, end='', flush=True)
    print()