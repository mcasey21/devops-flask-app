from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Hello World, I am a Flash app!</p> <a href="/about">Click here</a>'

@app.route('/about')
def about_page():
	return '<p>This is the about page</p>'
