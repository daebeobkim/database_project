from flask import Flask, render_template
import pymysql
from flask_socketio import SocketIO
import time

socketio = SocketIO(logger=True,engineio_logger=True)


db = pymysql.connect(host="192.168.0.40", user="root", passwd="1234", db="CAP2", charset="utf8")
cur = db.cursor()
sql = 'SELECT * from han'
cur.execute(sql)

data_list = cur.fetchall()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',data_list=data_list)
    


host_addr = "0.0.0.0"
port_num = "5000"

if __name__ == '__main__':
    app.run(host=host_addr,port=port_num,debug=True)
    
