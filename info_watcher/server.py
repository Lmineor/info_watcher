from flask import Flask, request, jsonify
import json
import os

from info_watcher.logger.logger import logger
from info_watcher.pipline.Youzheng import bump
from info_watcher.pipline.haidian import haidian_bump
from info_watcher.bark.messages import Bark

app = Flask(__name__)
code_map = {"youzheng": "邮政", "haidian": "海淀区人民政府信息公开"}


@app.route('/push', methods=['POST'])
def post_diff():
    # 获取当前请求数据
    body = request.get_json() or {}

    scene = body['scene']
    current_data = body['data']

    if scene == "youzheng":
        diffs = bump(current_data)
    elif scene == "haidian":
        diffs = haidian_bump(current_data)
    else:
        logger.error("unknown scene")
        diffs = None
    b = Bark(code_map)
    messages = {scene: diffs}
    b.notify_app(messages)

    response = {
        "msg": "ok",
        "code": 200,
        "diffs": diffs
    }
    # 返回响应
    return jsonify(response)


@app.route('/ping', methods=['GET'])
def ping():
    response = {
        "msg": "pong"
    }
    # 返回响应
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
