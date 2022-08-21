from flask import Flask, send_file

app = Flask(__name__)

@app.route('/logo')
def logo():
    send_file('/static/logo.png')


if __name__ == '__main__':
    app.run('0.0.0.0', '8880')