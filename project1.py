import csv
data = open('C:/Users/rlaeo/OneDrive/바탕 화면/travel.csv','rt',encoding='cp949') #지역 명소 데이터
travel = csv.reader(data)
next(travel)

mx=0
rate=0

def Classification():
    menu = input("자연명소, 체험관, 공원박물관, 문화재, 기차역, 키즈카페, 공방, 코스, 전통사찰, 영화드라마촬영지, 문화공간 중 하나를 입력하시오\n")
    for row in travel:
        for i in range(3,4):
            if menu == row[i]:
                if menu == "자연명소":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "체험관":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "공원박물관":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "문화재":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "기차역":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "키즈카페":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "공방":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "코스":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "전통사찰":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "영화드라마촬영지":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                elif menu == "문화공간":
                    print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                
def place():
    menu = input("찾고싶은 지역을 입력하시오\n")
    for row in travel:
        for i in range(6,7):
            split = row[6].split()
            if split[1] == "진주시":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "진양호로":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "명석면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "가좌동":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "내동면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "정촌면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "산유로":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "이반성면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "금산면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "진성면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "이반성면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "천전동":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "남강로":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "대평면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "지수면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "판문오동길":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "상평동":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "이현동":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "칠암동":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "강남로":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "동진로":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "대곡면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "문산읍":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "주약동":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "광제산로":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "곤수로":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "충무공동":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            elif split[1] == "지수면":
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
while True:
    print("------메뉴------")
    print("1. 분류로 찾기")
    print("2. 위치로 찾기")
    print("3. 종료")
    i = input("원하시는 메뉴를 입력하세요\n")
    if i == '분류':
        Classification()
    elif i == '위치':
        place()
