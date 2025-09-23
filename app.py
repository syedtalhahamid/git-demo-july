from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post')
def post():
    return render_template("index.html")

@app.route('/poster')
def poster():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000)

