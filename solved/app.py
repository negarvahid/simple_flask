import flask
from flask import render_template
from forms import LoginForm
from flask import render_template, flash, redirect
app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'codecademy'

@app.route('/')
def hello():
  return render_template('app.html', title='Home')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)
#question: why are there two return statements?
#how are we distinguishing POST vs GET?


#what other routes &views do we need?
app.run(debug=True)

