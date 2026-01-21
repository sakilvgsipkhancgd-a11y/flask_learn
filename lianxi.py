from flask import Flask, render_template, request,jsonify,Response
import json
from typing import Union
import pymysql
import os
from dotenv import load_dotenv
from functools import wraps


load_dotenv()
#数据库配置参数
DB_CONFIG={
    'host':os.getenv('DB_HOST'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD'),
    'port':3306,
    'charset':'utf8mb4',
    'db':os.getenv('DB_NAME')
}
"""认证装饰器，此步骤可以将函数包装，从而在别处可以
使用，减少重复代码,此处将请求参数校验函数包装，在后面每个路由复用"""
def auth_re(f):#f代表被包装的函数
    @wraps(f)
    def decorated_function(args,kwargs):#这个是原函数，包括两个参数,这两个参数作用分别有各自的作用如下：
        #args是一个元组，返回所有的位置参数
        #kwargs是一个字典，返回所有的关键字参数

        r = request.json.get('r') if request.is_json else None
        if not r:
            return jsonify({'code':0,'msg':'参数错误'})
        if r != 'abcd1234':
            return jsonify({'code':1,'msg':'参数不合法'})
        return f(*args,**kwargs)#返回函数值
    return decorated_function#返回包装后的函数，返回函数而不是返回值的作用在于在别处使用时是函数而不是值
"""
这一步处理数据库连接，将数据库连接也封装为函数，以后只需创建函数对象操作数据库
"""
def get_db_connection():
    return pymysql.connect(**DB_CONFIG)#此处创建了一个
#数据库连接，并传入了预先的数据库参数，此时并没有创建连接对象，只是返回一个连接





"""
这里涉及到一个问题，就是with语句块结束后，conn会自动关闭，所以
如果要在某个路由或者某个函数中使用连接，必须重新连接，所以一般情况下
每个想要操作数据库的函数中都要重新连接数据库。"""



app = Flask(__name__)


@app.route('/Customers', methods=['POST'])
@auth_re
def Customers() -> Union[dict, Response]: # type: ignore


            with connection.cursor() as cursor:
                cursor.execute("SELECT prod_name FROM Products")
                m = cursor.fetchall()
                n = [row[0] for row in m]

                return jsonify({'code':0,'msg':'成功','data':n})

@app.route("/OrderItems",methods=['POST'])
def OrderItems():
    with pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        port=3306,
        charset='utf8mb4'

    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM OrderItems')
            r = cursor.fetchall()
            return jsonify ({'code':0,'msg':'成功获取','data':r})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

