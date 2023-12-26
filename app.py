from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # reference to thisfile
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# kind assignt the value 'sqllite' to the location "SQLALCHEMY_DATABASE_URI" in app's config instance (config return a Config instacne that quite interesting)
# /// is relative path, dont want to specify the exact location, just want it reside in the project location
# //// is absolute path
# everything is gonna be stored in test.db file

# initialize the database
db = SQLAlchemy(app)

@app.route('/') # you are going to pass in the URL string of your route

def index():    # function for that route
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

