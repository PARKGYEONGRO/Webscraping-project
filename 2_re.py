# 정규식 regular expression

# 예시
# 주민등록번호 030102-1111111
# 이메일 parkgyeongro@naver.com

import re

# p 는 pattern 
p = re.compile("ca.e") 
# . : 은 하나의 문자를 의미함 ex) ca r e, ca s e, ca v e
# ^ (^de): 문자열의 시작 ex) de sk, de stination
# $ (se$) : 문자열의 끝 ex) ca se, ba se


# m = p.match("caffe")
# # print(m.group()) # match되지 않으면 에러 발생
# if m:
#     print(m.group())
# else:
#     print('매칭 X')


# 함수 활용
def print_match(m):
    if m:
        print("m.group() :",m.group()) # 일치하는 문자열 반환
        print("m.string",m.string) # 입력받은 문자열, string은 변수라서 () 없음
        print("m.start() :",m.start()) # 일치하는 문자열 시작 index
        print("m.end() :",m.end()) # 일치하는 문자열 끝 index
        print("m.span() :",m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print('매칭 X')

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
#                         # 문자열의 처음부분 care 까지는 일치함
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# list = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(list)

"""
정리

1. p = re.compile("원하는 형태")
2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
4. list = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

원하는 형태 : 정규식
. : 은 하나의 문자를 의미함 ex) ca r e, ca s e, ca v e
^ (^de): 문자열의 시작 ex) de sk, de stination
$ (se$) : 문자열의 끝 ex) ca se, ba se
"""