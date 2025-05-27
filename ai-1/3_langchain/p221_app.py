from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(
    model='gpt-3.5-turbo-instruct',
    temperature=0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    verbose=True
)

res = llm("이단비 바보라고 노래를 지어줘 .")
print(res)