import csv
fee = open('C:/Users/rlaeo/OneDrive/바탕 화면/subwayfee.csv','rt',encoding='UTF8') #유무임별
time = open('C:/Users/rlaeo/OneDrive/바탕 화면/subwaytime.csv','rt',encoding='UTF8') #시간대별
feedata = csv.reader(fee)
timedata = csv.reader(time)
next(feedata)
next(timedata)
next(timedata)

def menu(i):
    if i == '1':
        place()
    elif i == '2':
        time()

def place():
    print("메뉴 선택후 지역 검색")
    print("1. 지역의 유무임 승하차 인원")
    print("2. 지역의 시간대별 이용 현황")
    print("3. 종료")
    menu = input("원하시는 메뉴를 선택하세요    (서울역, 시청, 종각, 동대문, 신설동)")
    if menu == '1':
        mx = 0
        rate = 0
        mx_station = ''
        menu1 = input()
        for row in fee:
            for i in range(4,8):
                row[i] = int(row[i])
                
                if menu1 == "서울":




def time():
    print("메뉴 선택후 시간 검색")
    print("1. 가장 많이 간 지역")
    print("2. 가장 많이 안간 지역")
    print("3. 종료")
    menu = input("원하시는 메뉴를 선택하세요")


while True:
    print("------메뉴------")
    print("1. 지역 바탕 정보 검색")
    print("2. 시간 바탕 정보 검색")
    print("3. 종료")
    i = input("원하시는 메뉴를 선택하세요")
    menu(i)