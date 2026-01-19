from flask import Flask, render_template, request,jsonify,Response
import json
from typing import Union
import pymysql
import os
from dotenv import load_dotenv


load_dotenv()



"""
这里涉及到一个问题，就是with语句块结束后，conn会自动关闭，所以
如果要在某个路由或者某个函数中使用连接，必须重新连接，所以一般情况下
每个想要操作数据库的函数中都要重新连接数据库。"""



app = Flask(__name__)
r = "abcd1234"

@app.route('/task', methods=['POST'])
def task() -> Union[dict, Response]: # type: ignore
    r = request.json.get('r')

    if not r:
        return jsonify({'code': 1,'msg': '参数错误'})
    if r != "abcd1234":
        return jsonify({'code': 2,'msg': '参数不合法'})
    if r == "abcd1234":
        with pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db=os.getenv('DB_NAME'),
            port=3306,
            charset="utf8mb4"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT prod_name FROM Products")
                m = cursor.fetchall()
                n = [row[0] for row in m]

                return jsonify({'code':0,'msg':'成功','data':n})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

