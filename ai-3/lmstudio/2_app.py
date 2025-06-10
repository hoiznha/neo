import lmstudio as lms

model = lms.llm()

#답변을 스트리밍으로 받아옴. 응답이 한번에 다 오지 않고, 한조각씩 받아올때마다 바로 출력
for fragment in model.respond_stream('What is the meaning of life?'):
    print(fragment.content, end='', flush = True)

print()