import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
res = requests.get(url,headers =headers)
print("응답코드 : ", res.status_code) # 200이면 정상
res.raise_for_status()


with open("nadocoding.html","w",encoding="utf8") as f :
    f.write(res.text)