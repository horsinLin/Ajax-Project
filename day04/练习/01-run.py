from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:horsin@123@localhost:3306/flask"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "loginUser"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True)
    passwd = db.Column(db.String(120))

    def __init__(self, username):
        self.username = username

    def to_dict(self):
        dic = {
            "username" : self.username,
            "passwd" : self.passwd
        }
        return dic

    def __repr__(self):
        return "<Users : %r>" % self.username

class Province(db.Model):
    __tablename__="province"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    proname = db.Column(db.String(30))
    cities = db.relationship("City", backref="province", lazy="dynamic")

    def __init__(self, proname):
        self.proname = proname

    def __repr__(self):
        return "<Province : %r>" % self.proname

    def to_dict(self):
        dic = {
            "id" : self.id,
            "proname" : self.proname
        }
        return dic

class City(db.Model):
    __tablename__="city"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cityname = db.Column(db.String(30))
    pro_id = db.Column(db.Integer, db.ForeignKey("province.id"))

    def __init__(self, cityname, pro_id):
        self.cityname = cityname
        self.pro_id = pro_id

    def __repr__(self):
        return "<City : %r>" % self.cityname

    def to_dict(self):
        dic = {
            "id" : self.id,
            "cityname" : self.cityname,
            "pro_id" : self.pro_id
        }
        return dic

@app.route('/01-ajax')
def ajax_views():
    return render_template('01-ajax.html')

@app.route('/01-server')
def server_01():
    uname = request.args.get("username")
    print(uname)
    user = Users.query.filter_by(username=uname).first()
    if user:
        return json.dumps(user.to_dict())
    else:
        dic = {
            'status' : '0',
            'msg' : '没有查到任何信息!'
        }
        return dic

@app.route('/02-province')
def province_views():
    return render_template('03-province.html')

@app.route('/loadPro')
def loadPro_views():
    provinces = Province.query.all()
    list = []
    for province in provinces:
        list.append(province.to_dict())
    return json.dumps(list)

@app.route('/loadCity')
def loadCity_views():
    pid = request.args.get("pid")
    cities = City.query.filter_by(pro_id=pid).all()
    list = []
    for city in cities:
        list.append(city.to_dict())
    return json.dumps(list)

@app.route('/crossdomain')
def crossdomain_views():
    return render_template('04-crossdomain.html')

@app.route('/02-server')
def server_02():
    return "show('这是server_02响应回来的数据')"

if __name__ == '__main__':
    app.run(debug=True)





