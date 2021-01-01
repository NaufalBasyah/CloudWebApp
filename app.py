from flask import Flask
from flask import render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html', pageTitle="Home Page")

@app.route('/test')
def testss():
    return render_template('test.html', pageTitle="Test Page")

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUs.html', pageTitle="About Us Page")


if __name__ == '__main__':
    app.run(debug=True)
