from flask import Flask, send_file, request

app = Flask(__name__)

@app.before_request
def before_request():
    print(request.headers)


@app.route('/')
def index():
    return ''

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Cache-Control'] = 'no-store'
    response.status = 123
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880)