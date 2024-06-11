from flask import Flask, request, render_template, redirect, session, flash, url_for, make_response
from werkzeug.utils import secure_filename
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'a558821e2e2e0e6abbf89bb8f29bc7dd94f9ad0ffc2e1d03ab45f69a9630b86a'


@app.route('/', methods=['POST', 'GET'])
def start_page():
    if request.method == 'POST':
        response = make_response(redirect(url_for('hello')))
        response.set_cookie('username', request.form.get('name'))
        return response
    return render_template("start.html")


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    username = request.cookies.get('username')
    if request.method == 'POST':
        res = make_response(redirect(url_for('start_page')))
        res.set_cookie('username', username, max_age=0)
        return res
    return f'hi {username}'
