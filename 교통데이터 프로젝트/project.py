import csv
fee = open('C:/Users/rlaeo/OneDrive/바탕 화면/subwayfee.csv','rt',encoding='UTF8')
time = open('C:/Users/rlaeo/OneDrive/바탕 화면/subwaytime.csv','rt',encoding='UTF8')
feedata = csv.reader(fee)
timedata = csv.reader(time)
next(feedata)
next(timedata)
next(timedata)

def menu(i):
    if i == '1':
        place()
    elif i == '2':
        season()

def place():
    print("메뉴 선택후 지역 검색")
    print("1. 지역의 유무임 승하차 인원")
    print("2. 지역의 시간대별 이용 현황")
    print("3. 종료")
    choice = input("원하시는 메뉴를 선택하세요")


def season():
    print("메뉴 선택후 계절 검색")
    print("1. 가장 많이 간 지역")
    print("2. 가장 많이 활동한 시간")
    print("3. 종료")
    choice = input("원하시는 메뉴를 선택하세요")


while True:
    print("------메뉴------")
    print("1. 지역바탕 정보 검색")
    print("2. 계절 바탕 정보 검색")
    print("3. 종료")
    i = input("원하시는 메뉴를 선택하세요")
    menu(i)