import lmstudio as lms

model = lms.embedding_model("text-embedding-nomic-embed-text-v1.5@q8_0")

embedding = model.embed('Hello World!')


