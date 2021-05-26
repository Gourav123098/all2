import requests
import json

def speak(strs):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(strs)



url = ('https://newsapi.org/v2/everything?q=apple&from=2021-05-20&to=2021-05-20&sortBy=popularity&apiKey=995281151f564969a24e293ade26d69a')

response = requests.get(url).text
res = json.loads(response)

art = res['articles']
for artical in art:
    a2 = artical['title']
    a3 = artical['description']
    print(f"{a2}\n")
    speak(a2)
    print(f"{a3}\n")
    speak(a3)
