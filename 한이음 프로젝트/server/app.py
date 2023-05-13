from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''
    <h1>이건 h1 제목</h1>
    <h2> 이건 p 본문</h2>
    <a href = http://flask.palletsprojects.com">Flask 홈페이지 바로가기</a>
    '''
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name,user_id):
    return f'hello {user_name}({user_id})!'

if __name__== '__main__':
    app.run(debug=True)