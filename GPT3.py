import os
import openai
from functions import trans_E2J, trans_J2E
import requests
DEEP_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
openai.api_key = API_KEY

question = "明日の献立"

# source_lang = 'JA'
# target_lang = 'EN'

# # パラメータの指定
# params = {
#             'auth_key' : DEEP_API_KEY,
#             'text' : question,
#             'source_lang' : source_lang, # 翻訳対象の言語
#             "target_lang": target_lang  # 翻訳後の言語
#         }

# # リクエストを投げる
# request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
# result = request.json()['translations'][0]['text']
result = trans_J2E(question)
prompt = result

response = openai.Completion.create(engine="davinci",
                                    prompt=prompt,
                                    max_tokens=100,
                                    temperature=0.5,
                                    echo=True)

res = response.choices[0].text
print(res)


# text = "Riemann Zeta function is a very important function in number theory."
text = res

source_lang = 'EN'
target_lang = 'JA'

# パラメータの指定
params = {
            'auth_key' : DEEP_API_KEY,
            'text' : text,
            'source_lang' : source_lang, # 翻訳対象の言語
            "target_lang": target_lang  # 翻訳後の言語
        }

# リクエストを投げる
request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
result = request.json()['translations'][0]['text']
print(f"質問: {question}")

print(f"翻訳前: {text}")
print(f"翻訳後: {result}")
