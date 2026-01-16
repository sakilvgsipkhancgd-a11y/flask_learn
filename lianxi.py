from flask import Flask, render_template, request,jsonify,Response
import json
from typing import Union
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
        return jsonify({'code': 0,'msg': '参数正确'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

