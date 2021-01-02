from flask import Flask
from flask import render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    imgs = ["img1.jpg","img2.jpg","img3.jpg","4.jpg","5.jpg","6.jpg"]
    return render_template('index.html', pageTitle="Home Page", imgs=imgs )

@app.route('/test')
def testss():
    return render_template('test.html', pageTitle="Test Page")

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUs.html', pageTitle="About Us Page")


if __name__ == '__main__':
    app.run(debug=True)
