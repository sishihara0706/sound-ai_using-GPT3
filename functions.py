import os
import openai

import requests
DEEP_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def trans_E2J(source):
    # パラメータの指定
    params = {
                'auth_key' : DEEP_API_KEY,
                'text' : source,
                'source_lang' : "EN", # 翻訳対象の言語
                "target_lang": "JA"  # 翻訳後の言語
            }

    # リクエストを投げる
    request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = request.json()['translations'][0]['text']
    
    return request.json()['translations'][0]['text']

def trans_J2E(source):
    # パラメータの指定
    params = {
                'auth_key' : DEEP_API_KEY,
                'text' : source,
                'source_lang' : "JA", # 翻訳対象の言語
                "target_lang": "EN"  # 翻訳後の言語
            }

    # リクエストを投げる
    request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = request.json()['translations'][0]['text']
    
    return request.json()['translations'][0]['text']
     
