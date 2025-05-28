from langchain.memory import ConversationBufferMemory

#chatOpenAI 에서 사용하는 채팅 메시지 리스트 형식으로 출력 
memory = ConversationBufferMemory(return_messages=True)
memory.chat_memory.add_user_message("배고프다")
memory.chat_memory.add_ai_message("밥먹으러 어디 갈까?")
memory.chat_memory.add_user_message("라면 먹으러 가자")
memory.chat_memory.add_ai_message("지하철역 옆에 있는 분식집으로 가자.")
memory.chat_memory.add_user_message("그럼 출발!")
memory.chat_memory.add_ai_message("ok !!")

print(memory.load_memory_variables({}))
