import csv
data = open('C:/Users/rlaeo/OneDrive/바탕 화면/travel.csv','rt',encoding='cp949') #지역 명소 데이터
travel = csv.reader(data)
next(travel)

def Classification():
    menu = input("자연명소, 체험관, 공원박물관, 문화재, 기차역, 키즈카페, 공방, 코스, 전통사찰, 영화드라마촬영지, 문화공간 중 하나를 입력하시오\n")
    for row in travel:
        for i in range(3,4):
            object = row[i]
            if menu == object:
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
            
                
def place():
    menu = input("찾고싶은 지역을 입력하시오\n")
    count = 0
    for row in travel:
        for i in range(6,7):
            split = row[6].split()
            if menu == split[2]:
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                count += 1
           

            

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
    else:
        print("다시 입력해주세요")
