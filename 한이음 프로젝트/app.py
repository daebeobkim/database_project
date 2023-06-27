from flask import Flask, render_template, request
import pymysql

db = pymysql.connect(host="192.168.0.40", user="root", passwd="1234", db="CAP2", charset="utf8")
cur = db.cursor()
sql = 'SELECT * from han'
cur.execute(sql)

data_list = cur.fetchall()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # POST 요청 처리
        # 요청 파라미터 받기
        param = request.form.get('param_name')
        
        # 처리 로직 구현
        # ...

        return render_template('index.html', data_list=data_list, param=param)

    else:
        # GET 요청 처리
        # ...

        return render_template('index.html', data_list=data_list)

host_addr = "0.0.0.0"
port_num = "5000"

if __name__ == '__main__':
    app.run(host=host_addr, port=port_num, debug=True)
