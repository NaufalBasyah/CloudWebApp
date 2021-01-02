from flask import Flask
from flask import render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

categories = db.Table('category', db.metadata, autoload = True, autoload_with=db.engine)
products = db.Table('products', db.metadata, autoload = True, autoload_with=db.engine)

@app.route('/')
def index():
    ctg = db.session.query(categories).all()
    pd = db.session.query(products).all()
    return render_template('index.html', pageTitle="Home Page", ctg=ctg, pd=pd )

@app.route('/test')
def testss():
    return render_template('test.html', pageTitle="Test Page")

@app.route('/aboutUs')
def aboutUs():
    ctg = db.session.query(categories).all()
    return render_template('aboutUs.html', pageTitle="About Us Page", ctg=ctg)

@app.route('/category/<string:name>')
def filter_by_category(name):
    ctg = db.session.query(categories).all()
    for x in ctg:
        if x.cat_name==name:
            id= x.cat_id
    pd = db.session.query(products).filter_by(cat=id).all()
    return render_template('filtered.html', pageTitle="{{name}} Product Page", ctg=ctg, pd=pd , id=id)


if __name__ == '__main__':
    app.run(debug=True)
