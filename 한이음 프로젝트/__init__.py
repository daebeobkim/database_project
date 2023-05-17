from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from helloflask import Members

app = Flask(__name__)

# database 설정파일
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/testdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route("/one")
def home():
	member = Members.query.first()
	return 'Hello {0}, {1}, {2}, {3}, {4}'\
		.format(member.name, member.email, member.phone, member.start.isoformat(), member.end.isoformat())
	#return render_template('home.html')
    
@app.route('/all')
def select_all():
    members = Members.query.all()
    return render_template('db.html', members=members)