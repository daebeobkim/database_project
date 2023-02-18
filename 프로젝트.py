import csv #csv사용 모듈
import matplotlib.pyplot as plt
import platform

all = open('C:/Users/rlaeo/OneDrive/바탕 화면/소방scv/소방청_화재발생 정보.csv','rt',encoding='cp949') #전체
headoffice = open('C:/Users/rlaeo/OneDrive/바탕 화면/소방scv/소방관할관서.csv','rt',encoding='cp949') #소방본부 데이터
Area = open('C:/Users/rlaeo/OneDrive/바탕 화면/소방scv/행정구역.csv','rt',encoding='cp949') #지역 위주 데이터

all1 = csv.reader(all)
headoffice1 = csv.reader(headoffice)
Area1 = csv.reader(Area)
서울 = 0
경기=0
강원=0
전남=0
전북=0
경남=0
경북=0
충남=0
충북=0
인천=0
부산=0
울산=0
대구=0
광주=0
대전=0
세종=0
제주 = 0
sum=0
for row in all1:
    sum+=1
    if row[1] == '전라북도':
        전남 += 1
    elif row[1] == '서울특별시':
        서울 += 1
    elif row[1] == '경상남도':
        경남 += 1
    elif row[1] == '경상북도':
        경북 += 1
    elif row[1] == '전라남도':
        전남 += 1
    elif row[1] == '경기도':
        경기 += 1
    elif row[1] == '강원도':
        강원 += 1
    elif row[1] == '충청남도':
        충남 += 1
    elif row[1] == '충청북도':
        충북 += 1
    elif row[1] == '인천광역시':
        인천 += 1
    elif row[1] == '부산광역시':
        부산 += 1
    elif row[1] == '광주광역시':
        광주 += 1
    elif row[1] == '울산광역시':
        울산 += 1
    elif row[1] == '대구광역시':
        대구 += 1
    elif row[1] == '대전광역시':
        대전 += 1
    elif row[1] == '제주특별자치도':
        제주 += 1
    elif row[1] == '세종특별자치시':
        세종 += 1
    
print("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" %(전남, 서울, 경남, 경북, 전남, 경기, 충남 ,충북,인천,부산,광주,울산,대구,대전,제주,세종,강원))
print("%s" %(전남+서울+경남+경북+전남+경기+충남+충북+인천+부산+광주+울산+대구+대전+제주+세종+강원))

"""
ratio = [전남, 서울, 경남, 경북, 전남, 경기, 충남 ,충북,인천,부산,광주,울산,대구,대전,제주,세종,강원]
labels = ["전남", "서울", "경남", "경북", "전남", "경기", "충남" ,"충북","인천","부산","광주","울산","대구","대전","제주","세종","강원"]
plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()
"""
plt.rc('font', family='Malgun Gothic') 
지역 = [전남, 서울, 경남, 경북, 전남, 경기, 충남 ,충북 ,인천 ,부산 ,광주 ,울산 ,대구 ,대전 ,제주,세종,강원]
ticklabel=["전남", "서울", "경남", "경북", "전남", "경기", "충남" ,"충북","인천","부산","광주","울산","대구","대전","제주","세종","강원"]
plt.bar(ticklabel,지역)

plt.show()
