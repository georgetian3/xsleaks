from flask import Flask, send_file, Response

app = Flask(__name__)


@app.route('/')
def index():
    return send_file('static/target.html')

@app.route('/logo')
def logo():

    resp = send_file('static/logo.png')
    print(resp)
    return resp

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    response.cache_control.public = True
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run('0.0.0.0', '8880')
