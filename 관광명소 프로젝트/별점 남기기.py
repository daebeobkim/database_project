import pymysql

"""
conn = pymysql.connect(host='127.0.0.1',user='root',password='0000',db='stardb',charset='utf8')
cur = conn.cursor()
cur.execute("CREATE TABLE userTable (name char(20), grade float(2,1), line char(200))")
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
"""
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

 
