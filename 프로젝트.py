import csv #csv사용 모듈
all = open('C:/Users/rlaeo/OneDrive/바탕 화면/소방scv/소방청_화재발생 정보.csv','rt',encoding='cp949') #전체
headoffice = open('C:/Users/rlaeo/OneDrive/바탕 화면/소방scv/소방관할관서.csv','rt',encoding='cp949') #소방본부 데이터
Area = open('C:/Users/rlaeo/OneDrive/바탕 화면/소방scv/행정구역.csv','rt',encoding='cp949') #지역 위주 데이터

all1 = csv.reader(all)
headoffice1 = csv.reader(headoffice)
Area1 = csv.reader(Area)


for row in headoffice:
    for i in range(5):
        print(row[1][1])
