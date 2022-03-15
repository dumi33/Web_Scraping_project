import re
p = re.compile("ca.e")

def print_match(m) :
    if m :
        print("m.group() : ", m.group()) # 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())# 일치하는 문자열의 시작 / 끝 index
    else :
        print("매칭되지않음")

m = p.match("good cafe")
print_match(m)

m = p.search("good care")
print_match(m)

lst = p.findall("good care cafe")
print(lst)