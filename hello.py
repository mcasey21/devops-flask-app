from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Welcome!</p> <a href="/about">About Page</a> <a href="/contact">Contact Page</a>'

@app.route('/about')
def about_page():
	return '<p>This is the about page</p>'

@app.route('/contact')
def contact_page():
	return '<p>My Email: C23343691@mytudublin.ie'
