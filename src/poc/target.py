from flask import Flask, request, Response, make_response

app = Flask(__name__)

@app.route('/exists')
def exists():
    return 'exists'

@app.route('/does_not_exist')
def does_not_exist():
    return 'does not exist'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8880)