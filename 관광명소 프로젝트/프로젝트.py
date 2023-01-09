import csv #csv사용 모듈
from haversine import haversine #위도경도 사용 모듈
data = open('C:/Users/rlaeo/OneDrive/바탕 화면/travel.csv','rt',encoding='cp949') #지역 명소 데이터
bus = open('C:/Users/rlaeo/OneDrive/바탕 화면/bus.csv','rt',encoding='cp949') #버스정류장 위도경도 데이터
travel = csv.reader(data)
busstop = csv.reader(bus)
next(travel) #row 첫번째 줄을 생략 
next(busstop)


def Distance():#버스정류장 기준 위도 경도를 사용해 거리 계산
    global a,b,c,d
    nearby  = input("현재 위치에서 가까운 버스정류장을 입력하세요\n")
    distant = input("목적지 근처의 버스정류장을 입력하세요\n")
    for row in busstop:     
        for i in range(2,3):
            Latitude = row[i]
            longitude = row[i]
            if nearby == Latitude:
                a = float(row[3])#출발지 경도
                b = float(row[4])#출발지 위도
            elif distant == longitude:
                c = float(row[3])#도착지 경도
                d = float(row[4])#도착지 위도
    start = (b,a)
    end = (d,c)
    answer = haversine(start,end,unit='km')
    print(round(answer,2),"km")


def Classification(): #분류 입력으로 데이터 찾기
    menu = input("자연명소, 체험관, 공원박물관, 문화재, 기차역, 키즈카페, 공방, 코스, 전통사찰, 영화드라마촬영지, 문화공간 중 하나를 입력하시오\n")
    for row in travel: #row와 column으로 이루어진 2차원데이터를 반복해 찾음
        for i in range(3,4): #찾은 데이터를 1차원데이터로 반복해 찾음
            object = row[i]
            if menu == object:
                print("관광지명: %s \n이용시간: %s 주소: %s 전화번호 %s\n" %(row[5],row[4],row[6],row[7]))
                          
def place(): #지역 입력으로 데이터 찾기
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
    print("3. 버스정류장으로 목적지 까지 거리 계산하기")
    print("4. 종료")
    i = input("원하시는 메뉴를 입력하세요\n")
    if i == '1':
        Classification()
    elif i == '2':
        place()
    elif i == '3':
        Distance()
    elif i == "4":
        break
    else:
        print("다시 입력해주세요")
