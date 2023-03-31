import flask
from flask import render_template
#import forms
from flask import render_template, flash, redirect

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'codecademy'

@app.route('/')
def hello():
  return render_template('app.html', title='Home')
@app.route('/login', methods=['GET', 'POST'])
def login():
    #use forms
    pass




#question: why are there two return statements?
#how are we distinguishing POST vs GET?


#what other routes &views do we need?
app.run(debug=True)

