from flask import Flask, render_template
import pymysql

db = pymysql.connect(host="192.168.0.40", user="root", passwd="1234", db="CAP2", charset="utf8")
cur = db.cursor()
sql = 'SELECT * from han'
cur.execute(sql)

data_list = cur.fetchall()

print(data_list[0])
print(data_list[1])
print(data_list[2])

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',data_list=data_list)
    
host_addr = "0.0.0.0"
port_num = "5000"

if __name__ == '__main__':
    app.run(host=host_addr,port=port_num,debug=True)
    
