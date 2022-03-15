import requests
res = requests.get("http://google.com")
print("응답코드 : ", res.status_code) # 200이면 정상
res.raise_for_status()

# if res.status_code == requests.codes.ok :
#     print("정상입니다.")
# else :
#     print("문제가 생겼습니다.")

with open("mygoogle.html","w",encoding="utf8") as f :
    f.write(res.text)