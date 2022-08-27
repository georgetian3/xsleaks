from flask import Flask, send_file, request, Response

app = Flask(__name__)

@app.before_request
def before_request():
    #print(request.headers)
    pass


@app.route('/')
def index():
    print('status', request.status)
    resp = Response
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Cache-Control'] = 'no-store'
    resp.status = 123
    return 'test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880)