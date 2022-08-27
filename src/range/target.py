from flask import Flask, request, Response, make_response

app = Flask(__name__)

@app.before_request
def before_request():
    #print(request.headers)
    pass


@app.route('/')
def index():
    print('status', request.get_json())    
    return 'test', 123

""" @app.after_request
def headers(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Cache-Control'] = 'no-store'
    print(resp)
    return resp """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880)