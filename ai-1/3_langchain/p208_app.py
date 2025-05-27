from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI
import os

serpapi_api_key=os.environ.get('SERPAPI_API_KEY')

tools = load_tools(["serpapi","llm-math"], llm=OpenAI(
        model = 'gpt-3.5-turbo-instruct',
        temperature = 0,
    ),
    serpapi_api_key = serpapi_api_key
)

agent = initialize_agent(
    agent = "zero-shot-react-description",
    llm = OpenAI(
        model='gpt-3.5-turbo-instruct',
        temperature=0,
    ),
    tools = tools,
    verbose = True
)

print('-' * 50)
input_agent = "123 * 4 를 계산기로 계산하세요."
agent.run(input_agent)

print('-' * 50)
input_agent = "오늘 한국 날씨를 웹 검색으로 확인하세요."
agent.run(input_agent)