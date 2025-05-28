import openai
from IPython.display import Image, display

response =openai.Image.create(
    prompt="Happy robots playing in the playground",
    n=1,
    size="512x512"
)

for data in response['data']:
    images_url = data['url']
    print(images_url)
    display(Image(url=images_url))
    print('-'*50)