import openai
import os
import deepl
import tiktoken

def summarize_text(user_text, lang='en'):
    if lang == 'en':
        messages = [
            {"role": "user", "content": "You are a helpful assistant in the summary."},
            {"role": "user", "content": f"Summarize the following text:\n{user_text}"},
    ]
    elif lang == 'ko':
        messages = [
            {"role": "user", "content": "당신은 요약을 도와주는 유용한 조수입니다."},
            {"role": "user", "content": f"다음 글을 요약해 주세요:\n{user_text}"},
    ]
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = messages,
        max_tokens=500,
        temperature =0.3,
        n=1
    )

    summary = response.choices[0].message['content']

    return summary

def summarize_text_final(text_list, lang='en'):
    joined_summary = ' '.join(text_list)

    enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
    token_num = len(enc.encode(joined_summary))

    req_max_token = 2000
    final_summary = ''

    if token_num < req_max_token:
        final_summary = summarize_text(joined_summary,lang)

    return token_num, final_summary

def translate_english_to_korean_using_openAI(text):
    user_content = f"Translate the follwing English senetence into korean.\n {text}"
    message = [
        {"role":"user", "content":user_content}
    ]

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = message,
        max_tokens=2000,
        temperature=0.3,
        n = 1
    )

    assistant_reply = response.choices[0].message["content"]

    return assistant_reply

def translate_english_to_korean_using_deepl(text):
    translator = deepl.Translator(os.getenv('DEEPL_API_KEY'))
    result = translator.translate_text(text, target_lang='KO')

    return result.text
