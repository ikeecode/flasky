from flask import Flask
from flask import request
from flask import redirect
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
	header = request.headers.get('User-Agent')
	return '<h1> Mahamadou Kaba : ikeecode in {} </h1>'.format(header), 400


@app.route('/red/<name>')
def red(name):
	return redirect('https://www.{}.com'.format(name))

@app.route('/istme')
def istme():
	infos = {
	'name':"Mahamadou Kaba",
	'age' :"24",
	'hobbies':['Japanese Animations', 'Programming', 'AI in python']
	}
	return render_template('me.html', infos = infos)
