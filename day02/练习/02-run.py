from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:horsin@123@localhost:3306/flask"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class loginUser(db.Model):
    __tablename__ = "loginUser"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True)
    passwd = db.Column(db.String(120))

    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def __repr__(self):
        return "<loginUser: %r>" % self.username

db.create_all()

@app.route('/login')
def login_views():
    return render_template('06-login.html')

@app.route('/server', methods=['POST'])
def server_views():
    username = request.form['username']
    user = loginUser.query.filter_by(username=username).first()
    if user:
        return "找到用户名为 %s 的账户" % user.username
    else:
        return "找不到该用户!"

if __name__ == '__main__':
    app.run(debug=True)