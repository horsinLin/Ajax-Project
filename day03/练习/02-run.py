from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:horsin@123@localhost:3306/flask"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Province(db.Model):
    __tablename__ = "province"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    proname = db.Column(db.String(30), nullable=False)
    cities = db.relationship("City", backref="province", lazy="dynamic")

    def __init__(self, proname):
        self.proname = proname

    def to_dict(self):
        dic = {
            'id' : self.id,
            'proname' : self.proname
        }
        return dic

    def __repr__(self):
        return "<Province : %r>" % self.proname

class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cityname = db.Column(db.String(30), nullable=False)
    pro_id = db.Column(db.Integer, db.ForeignKey("province.id"))

    def __init__(self, cityname, pro_id):
        self.cityname = cityname
        self.pro_id = pro_id

    def to_dict(self):
        dic = {
            'id' : self.id,
            'cityname' : self.cityname,
            'pro_id' : self.pro_id
        }
        return dic

    def __repr__(self):
        return "<City : %r>" % self.cityname

db.create_all()

@app.route('/province')
def province_views():
    return render_template('03-province.html')

@app.route('/loadPro')
def loadPro_views():
    provinces = Province.query.all()
    list = []
    for pro in provinces:
        list.append(pro.to_dict())
    return json.dumps(list)

@app.route('/loadCity')
def loadCity_view():
    pid = request.args.get('pid')
    cities = City.query.filter_by(pro_id=pid).all()
    list = []
    for city in cities:
        list.append(city.to_dict())
    return list

if __name__ == "__main__":
    app.run(debug=True)
