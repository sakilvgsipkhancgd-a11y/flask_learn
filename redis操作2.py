import redis
#像连接数据库一样链接redis服务器
from flask import Flask,jsonify,request
import pymysql
import hashlib
import uuid
import json
r = redis.Redis(
    host='localhost',

    port=6379,
    db=0,
    decode_responses=True
    )


app = Flask(__name__)
@app.route('/task',methods=['POST'])
def task():
    """
    请求的数据格式要求：{"ordered_string":"xxxx"}
    returns:
    """
    ordered_string = request.json.get('ordered_string')
    if not ordered_string:
        return jsonify({"status":False,"error":"参数错误"})

#生成任务ID
    tid = str(uuid.uuid4())

#将任务存入Redis队列
    task_dict = {'tid':tid,'data':ordered_string}
    r.lpush('task_queue',json.dumps(task_dict))
#返回任务ID给客户端
    return jsonify({"status":True,"data":tid,"message":"任务已提交,预计处理时间为10秒"})

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=2000)
