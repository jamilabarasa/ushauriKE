from config import app
from flask import render_template
from forms import RegisterForm

@app.route('/')
def index():
    form = RegisterForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)