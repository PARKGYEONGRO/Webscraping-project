# * requests 모듈 설치 필요 *
# pip 안 되면 환경변수 확인 또는 버젼 업글해보자
import requests


# 아래 두 개는 쌍으로 사용
res = requests.get("http://www.google.com")
res.raise_for_status() # 문제가 발생하면 코드를 끝내고 오류를 알려줌


# if res.status_code == requests.ccodes.ok:
#     print('정상입니다.')
# else:
#     print('문제가 발생하였습니다. [에러코드 ',res.status_code, ']')
# print("응답코드 :", res.status_code) # 200 정상


# 해당 페이지의 글자 갯수
print(len(res.text))


print(res.text)

# 파일로 만들기
with open('mygoogle.html','w', encoding="utf8") as f:
    f.write(res.text) # res.text 의 내용을 'mygoogle.html'파일로 만들어줌