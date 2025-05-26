import openai

response = openai.Moderation.create(
    input="i fuck you.",
)
print(response)