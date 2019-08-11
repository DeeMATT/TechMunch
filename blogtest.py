from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, UpdateForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5f6be4d21f121d9ec8124d997d985888'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/submit', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template(register.html, )


if __name__ == '__main__':
    app.run(debug=True)