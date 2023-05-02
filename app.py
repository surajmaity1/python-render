from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This app is running ...'

if __name__ == '__main__':
    app.run()