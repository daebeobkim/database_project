import csv
data = open('C:/Users/rlaeo/OneDrive/바탕 화면/travel.csv','rt',encoding='UTF8') #데이터
travel = csv.reader(data)
next(travel)

mx=0
rate=0
travel=''

for row in data:
    for i in range(1,8):
        row[i] = int(row[i])
    if row[4] == "자연명소":
        print(row[1])
