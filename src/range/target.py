from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return ''

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880)