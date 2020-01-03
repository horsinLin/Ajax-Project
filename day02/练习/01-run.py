from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/01-getxhr')
def getxhr():
    return render_template('01-getxhr.html')

@app.route('/02-get')
def get_views():
    return render_template('02-get.html')

@app.route('/03-get')
def get03_view():
    return render_template('03-get.html')

@app.route('/02-server')
def server02_views():
    return "这是AJAX的请求"

@app.route('/03-server')
def server03_views():
    uname = request.args.get('uname')
    return "欢迎: "+uname

@app.route('/04-post')
def post_views():
    return render_template('04-post.html')

@app.route('/04-server', methods=['POST'])
def server04_views():
    uname = request.form['uname']
    return uname

@app.route('/05-post')
def post05_views():
    return render_template('05-post.html')

if __name__ == '__main__':
    app.run(debug=True)