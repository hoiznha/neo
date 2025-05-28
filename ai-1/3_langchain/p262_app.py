import os
from langchain.agents import load_tools
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

google_cse_id = os.environ.get("GOOGLE_CSE_ID")
google_api_key = os.environ.get("GOOGLE_API_KEY")

#도구 준비
tools = load_tools(
    tool_names = ["serpapi","llm-math"],
    llm = ChatOpenAI(
        model = "gpt-3.5-turbo-instruct",
        temperature = 0
    )
)

#메모리 생성
memory = ConversationBufferMemory(
    memory_key = "chat_history",
    return_messages = True,
)

# 에이전트 생성
agent = initialize_agent(
    agent = "zero-shot-react-description",
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature = 0
    ),
    tools = tools,
    verbose = True,
    memory = memory
)

print(agent.run("좋은 아침입니다."))
print('-'*50)

print(agent.run("우리집 반려견 이름은 다온이입니다."))
print('-'*50)

print(agent.run("우리집 반려견 이름을 불러주세요."))
print('-'*50)
