from flask import Flask, render_template
import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="0000", db="practice", charset="utf8")
cur = db.cursor()
sql = 'SELECT * from customer'
cur.execute(sql)

data_list = cur.fetchall()

print(data_list[0])
print(data_list[1])
print(data_list[2])

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',data_list=data_list)
    
if __name__ == '__main__':
    app.run()
    
