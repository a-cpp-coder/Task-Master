from flask import Flask

app = Flask(__name__) # reference to thisfile

@app.route('/') # you are going to pass in the URL string of your route

def index():    # function for that route
    return "Hello Huy! - test"   

if __name__ == "__main__":
    app.run(debug=True)

