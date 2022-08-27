from flask import Flask, request, Response, make_response

app = Flask(__name__)


@app.route('/')
def index():
    print('status', request.get_json()['status'])    
    return 'test', 201

""" @app.after_request
def headers(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Cache-Control'] = 'no-store'
    print(resp)
    return resp """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880)