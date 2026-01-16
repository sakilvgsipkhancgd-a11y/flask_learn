from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return "欢迎来到我的第一个网站，永远爱你我的宝贝"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)