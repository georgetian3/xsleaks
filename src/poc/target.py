from flask import Flask, request, Response, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'exists'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880)