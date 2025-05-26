from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex, ServiceContext, LLMPredictor
from langchain.chat_models import ChatOpenAI

documents = SimpleDirectoryReader('data').load_data()

llm_predictor = LLMPredictor(llm=ChatOpenAI(
    temperature=0, 
    model_name="gpt-3.5-turbo"
))

ServiceContext = ServiceContext.from_defaults(
    llm_predictor=llm_predictor
)

index = GPTVectorStoreIndex.from_documents(documents, service_context=ServiceContext)

# ---기본 셋업 -----

query_engine = index.as_query_engine()

print('-'*50)
print(query_engine.query("미코의 소꿉친구 이름은?"))

print('-'*50)
print(query_engine.query("울프 코퍼레이션의 CEO는 누구야?"))

print('-'*50)
print(query_engine.query("미코의 성격은?"))
