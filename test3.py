
from fastapi import FastAPI,requests
import uvicorn
import json
#创建FastAPI的实例对象
app=FastAPI()

BASE_URL = '/test/'

# 接收get请求
# @app.routes(BASE_URL + 'get/test', methods=['GET','POST'])
@app.get(BASE_URL + 'hello')
def test_get():
    # 解析请求参数
    # param = requests.args.to_dict()
    # name = param['name']
    # password = param['password']
    result = {
        'msg': "Welcome! " + "name"
    }
    # 返回json
    result_json = json.dumps(result)
    return result_json


# 接收post请求
# @app.routes(BASE_URL + 'post/test', methods=['POST','GET'])
@app.get(BASE_URL + 'hello2')
def test_post():
    # 解析请求参数
    data = requests.get_data()
    print(type(data))
    json_data = json.loads(data.decode("utf-8"))
    name = json_data['name']
    password = json_data['password']
    result = {
        'msg': "welcome! " + name
    }
    # 返回json
    result_json = json.dumps(result)
    return result_json



if __name__ == '__main__':
    #加上这个就可以在运行main.py文件时，就运行uvicorn服务
    uvicorn.run(app="test3:app",host="0.0.0.0",port=5000)