from flask import Flask, request, render_template, url_for, redirect
from flask_wtf.csrf import CSRFProtect
from HW_3.model import db, User
from HW_3.form import NewUser

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SECRET_KEY'] = b'36e3dbd6e3732b5c8f5c96479e159da73c1a6dcaa549aa6445486129bfb729b4'
db.init_app(app)
csrf = CSRFProtect(app)

"""
@app.cli.command('init_db')
def init_db():
    db.create_all()
    print('ok')
"""


@app.route('/', methods=['POST', 'GET'])
def index():
    form = NewUser()
    if request.method == 'POST' and form.validate():
        db.create_all()
        new_user = User(name=form.name.data,
                        surname=form.surname.data,
                        password=form.password.data,
                        email=form.email_user.data)
        db.session.add(new_user)
        db.session.commit()
    return render_template('form.html', form=form)


if __name__ == '__main__':

    app.run(debug=True)

