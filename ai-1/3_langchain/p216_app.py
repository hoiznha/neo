import langchain
from langchain.cache import InMemoryCache
from langchain.llms import OpenAI

llm = OpenAI(
    model='gpt-3.5-turbo-instruct',
    temperature=0,
)

langchain.llm_cache = InMemoryCache()

print(llm.generate(["하늘의 색깔은?"]))
#캐쉬 사용 -> 토큰사용 x, 모델 사용x , 항상 같은 결과 
print(llm.generate(["하늘의 색깔은?"]))
