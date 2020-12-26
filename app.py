from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/test')
def testss():
    return "testing testing"


if __name__ == '__main__':
    app.run(debug=True)
