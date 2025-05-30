import requests
import os
import textwrap

def summarize_contents(contents_url, target_language):
    KAGI_API_KEY = os.environ["KAGI_API_KEY"]

    api_url = "https://kagi.com/api/v0/summarize"
    headers = {"Authorization" : "Bot " + KAGI_API_KEY}
    parameters = {"url": contents_url, "target_language": target_language}

    response = requests.get(api_url, headers=headers, params=parameters)

    summary = response.json()['data']['output']
    return summary

contents_url = 'https://www.youtube.com/watch?v=Ks-_Mh1QhMc'
target_language = 'KO'

try:
    summary = summarize_contents(contents_url, target_language)
    print('[콘텐츠 URL]' , contents_url)
    print('- 요약 내용(축약) : ', textwrap.shorten(summary, width=150, placeholder=' [...이하 생략 ...]'))
except Exception as e:
    print(f"알 수 없는 오류 발생: {e}")

