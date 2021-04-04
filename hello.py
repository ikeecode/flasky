from flask import Flask
from flask import request
from flask import redirect 


app = Flask(__name__)

@app.route('/')
def index():
	header = request.headers.get('User-Agent')
	return '<h1> Mahamadou Kaba : ikeecode in {} </h1>'.format(header), 400


@app.route('/red/<name>')
def red(name):
	return redirect('https://www.{}.com'.format(name))

