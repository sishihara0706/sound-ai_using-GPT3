import openai

import os
import cv2
import pprint
import sys
import time
from functions import trans_E2J, trans_J2E
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
openai.api_key = API_KEY
prompt = input("画像を生成します。テーマを適当に入力してください。（例）「京都の街並み」>>")
en_prompt = trans_J2E(prompt).replace(" ","-")
# sys.exit()
response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)

download_file(image_url, f"./{en_prompt}.jpg")

img = cv2.imread(f"./{en_prompt}.jpg")
cv2.imshow(f"{en_prompt}",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
