from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)


@app.route('/mypage/me')
def kid_1():
    return render_template('me.html')

@app.route('/mypage/contact', methods=['GET','POST'])
def kid_2():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == "POST":
        print(request.form)
        return redirect("/mypage/me")