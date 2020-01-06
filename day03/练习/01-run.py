from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import json

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:horsin@123@localhost:3306/flask"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    uname = db.Column(db.String(50))
    upwd = db.Column(db.String(50))
    realname = db.Column(db.String(30))

    # 将当前对象中的所有属性封装到一个字典中
    def to_dict(self):
        dic = {
            "id" : self.id,
            "uname" : self.uname,
            "upwd" : self.upwd,
            "realname" : self.realname
        }
        return dic

    def __init__(self,uname,upwd,realname):
        self.uname = uname
        self.upwd = upwd
        self.realname = realname

    def __repr__(self):
        return "<Users : %r>" % self.uname

@app.route('/json')
def json_views():
    # list = ["Fan Bingbing","Li Chen","Cui Yongyuan"]
    dic = {
        'name' : 'Bingbing Fan',
        'age' : 40,
        'gender' : "female"
    }
    uList = [
        {
            'name' : 'Bingbing Fan',
            'age' : 40,
            'gender' : "female"
        },
        {
            'name' : 'Li Chen',
            "age" : 40,
            "gender" : 'male'
        }
    ]
    # jsonStr = json.dumps(list)
    jsonStr = json.dumps(dic)
    return jsonStr

@app.route('/page')
def page_views():
    return render_template('01-page.html')

@app.route('/json_users')
def json_users():
    # user = Users.query.filter_by(id=1).first()
    # print(user)
    # return json.dumps(user.to_dict())
    users = Users.query.filter_by(id=1).all()
    print(users)
    list = []
    for user in users:
        list.append(user.to_dict())
    return json.dumps(list)

@app.route('/show_info')
def show_views():
    return render_template('02-user.html')

@app.route('/server')
def server_views():
    users = Users.query.filter().all()
    list = []
    for user in users:
        list.append(user.to_dict())
    return json.dumps(list)

@app.route('/load')
def load_views():
    return render_template('04-load.html')

@app.route('/load_server')
def load_server():
    return "这是使用jquery的load方法发送的请求"

if __name__ == "__main__":
    app.run(debug=True)