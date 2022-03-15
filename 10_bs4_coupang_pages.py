import requests
import re
from bs4 import BeautifulSoup


for i in range(1,6) :

    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)
    #print("페이지 : ", i)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    items = soup.find_all("li",attrs = {"class" : re.compile("^search-product")})
    for item in items : 

        # 광고 제품은 제외
        ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
        if ad_badge :
            #print("<광고 상품은 제외합니다.>")
            continue

        
        # 제품명
        name = item.find("div",attrs = {"class" : "name"}).get_text()
        if ("LG" not in name) and ("삼성" not in name)  :
            #print("LG, 삼성 제품만 출력합니다.")
            continue
        # 가격
        price = item.find("strong",attrs = {"class" : "price-value"}).get_text()
        
        # 평점
        star = item.find("em",attrs = {"class" : "rating"})
        if star :
            star = star.get_text()
        else :
            #print("<평점 없는 상품 제외합니다>")
            continue
        # 평점수
        rate_cnt = item.find("span",attrs = {"class" : "rating-total-count"})  
        if rate_cnt :
            rate_cnt = rate_cnt.get_text()[1:-1]
        else :
           # print("<평점 수 없는 상품 제외합니다>")
            continue

        link = item.find("a",attrs = {"class" : "search-product-link"})["href"]

        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회 
        if float(star) >= 4.5 and int(rate_cnt) >= 100 : 
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점수 : {star}점 ({rate_cnt})")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
