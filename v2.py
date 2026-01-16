#此版本加入基于文档的校验
from flask import Flask,jsonify,request
import pymysql
import hashlib

def get_user():
    info = {}#创建字典用来储存和解析的token和对应的名字
    with open('user.txt','r',encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            token,name = line.split(',')
            info[token] = name#前面已经创建了字典info，此处将token和name作为键值对放进字典中
    return info

app = Flask(__name__)
@app.route('/one',methods=['POST'])
def one():
    token = request.args.get('token')
    if not token:

        return jsonify({"status":False,"error":"请输入token"})#此处基础校验，验证用户有没有上传token过来，如果没有，直接提示错误
    user_dict = get_user():
    if token not in user_dict:
        return jsonify({"status":False,"error":"token不合法，请重新输入"})
    ordered_string =request.json.get('ordered_string')





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)