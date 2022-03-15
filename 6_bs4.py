import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력 
# print(soup.a.attrs) # a element의 속성정보 출력
#print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력 


# print(soup.find("a",attrs={"class" : "Nbtn_upload"})) #class =  "nbtn_upload"인 a element를(태그명 : "a") 찾아 
# print(soup.find(attrs={"class" : "Nbtn_upload"})) # class = "nbtn_upload" 인 어떤 element를 찾아줘 

rank1 = soup.find("li", attrs={"class" : "rank01"})
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling

print(rank1.parent.a.get_text())
rank2 = rank1.find_next_sibling("li") # li element를 가진 sibling찾기
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li") # li element를 가진 sibling찾기
print(rank3.a.get_text())
rank4 = rank3.find_previous_sibling("li") # li element를 가진 sibling찾기
print(rank4.a.get_text())

rank_all = rank1.find_next_siblings("li") # li element를 가진 sibling찾기
print(rank_all)


