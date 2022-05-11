import suanpan
from suanpan.app import app
from flask import Flask, abort, request, jsonify
from suanpan.app.arguments import Json, String, Int


def create_app():
    server = Flask(__name__)

    # 自定义接口
    @server.route('/test', methods=['GET'])
    def get_info():
        return jsonify({
            "success": True,
            "message": "",
            "data": "xuelang suanpan"
        })
    # 注意！！！ 一定要将server返回，交给suanpan app
    return server


def run_flask():
    web = create_app()
    # 注意！！！ 一定要将加下面的一行代码，将web交给suanpan app，否则无法访问http服务
    app._stream.sioLoop.setWebApp(web)


@app.afterInit
def init(context):
    # 启动http服务
    run_flask()


@app.input(Json(key="inputData1"))
@app.output(String(key="outputData1", alias='out1'))
def main(context):
    args = context.args
    return "sp"


if __name__ == '__main__':
    suanpan.run(app)
