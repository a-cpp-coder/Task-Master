from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # reference to thisfile
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# kind assignt the value 'sqllite' to the location "SQLALCHEMY_DATABASE_URI" in app's config instance (config return a Config instacne that quite interesting)
# /// is relative path, dont want to specify the exact location, just want it reside in the project location
# //// is absolute path
# everything is gonna be stored in test.db file

# initialize the database
db = SQLAlchemy(app)    # db is initialized with the setting from the app

class To_Do(db.Model):
    # the essential elements
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET']) # you are going to pass in the URL string of your route
def index():    # function for that route
    if request.method == 'POST':
        task_content = request.form['content']
        #create a To_Do object that's going to have its content = content of the input
        new_task = To_Do(content=task_content)

        # after having To_Do model, push it to the Database
        try:
            db.session.add(new_task)    # add to DB session
            db.session.commit()
            return redirect('/')        # back to the begin ?
        except:
            return "There was an issue adding your task"

    else:
        tasks = To_Do.query.order_by(To_Do.date_created).all()  # ? first()
        return render_template('index.html', tasks = tasks) # {{% for task in tasks %}} thi ra la the, qua ao

# set up a new route for the delete part
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = To_Do.query.get(id)
    # querry the DB to get the ID

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')    # redirect back to the homepage
    except:
        return "There was a problem deleting your task"

# another route for the update part
@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    task = To_Do.query.get(id)

    if request.method == 'POST':
        task.content = request.form['content']
        
        try:
            db.session.commit()     # no need more action, already change task.content
            return redirect('/')    # back to homepage
        except:
            return "There was an issue updating your task"
    else:
        return render_template('update.html', task = task)
    
if __name__ == "__main__":
    app.run(debug=True)

