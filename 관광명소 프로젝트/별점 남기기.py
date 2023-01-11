import pymysql

"""
conn = pymysql.connect(host='127.0.0.1',user='root',password='0000',db='stardb',charset='utf8') #전체 스키마 접속
cur = conn.cursor()
cur.execute("CREATE TABLE userTable (name char(20), grade float(2,1), line char(200))") #별점 테이블
cur.execute("CREATE TABLE Member (id VARCHAR(20), password VARCHAR(45), name VARCHAR(45), age INT(11))") #회원정보 테이블
"""

conn,cur = None,None
data1,data2,data3,data4 = "","","",""
sql = ""

conn = pymysql.connect(host='127.0.0.1',user='root',password='0000',db='stardb',charset='utf8')
cur = conn.cursor()
"""
while(True):
    data1 = input("명소 이름 ==> ")
    if data1 == "":
        break
    data2 = input("별점 입력하기 ==> ")
    data3 = input("후기 남기기 ==> ")
    sql = "INSERT INTO userTable VALUES('"+data1+"',"+data2+",'"+data3+"')"
    cur.execute(sql)
conn.commit()

cur.execute("SELECT * FROM userTable")

print("명소이름 별점 후기")
print("-----------------")
while(True):
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    print("%s %s %5s" %(data1,data2,data3))
conn.close()   
"""
def login():   
    print("로그인")
    id = input("id : ")
    password = input("password : ")
    cur.execute("SERECT id, name FROM member WHERE id = '%s' AND password = '%s'" %(id,password))
    row = cur.fetchall()
    if len(row) < 1:
        print("틀렸습니다 다시 입력해주세요")
        return id, 0
    if row[0][0] == id:
        print("%s님 환영합니다" %(row[0][1]))
        return id,1



def membership():
    print("*****회원가입*****")
    cur.execute("ALTER TABLE member CONVERT TO CHARSET utf8;")
    id = input("원하시는 ID를 입력하세요 : ")
    password = input("원하시는 비밀번호를 입력하세요 : ")
    name = input("이름을 입력하세요 : ")
    age = int(input("나이를 입력하세요 : "))
    cur.execute("INSERT INTO `member` (`id`, `password`, `name`, `age`) VALUES ('%s', '%s', '%s', '%d')" %(id, password, name, age))
    conn.commit()

while True:
    menu = input("메뉴를 선택하시오 : 1. 로그인  2. 회원가입")
    if menu == '1':
        login()
    elif menu == '2':
        membership()