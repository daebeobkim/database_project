import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',password='0000',db='solodb',charset='utf8')
cur = conn.cursor()


cur.execute("INSERT INTO userTable VALUES('hong','홍지윤','hong@naver.com',1996)")
conn.commit()