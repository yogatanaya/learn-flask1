from flask import Flask, render_template, request, flash 

app = Flask(__name__)
app.secret_key = "tyogaappsample_889"

@app.route('/hello')
def index():
	flash("Whats your name?")
	return render_template('index.html') 

@app.route('/greet', methods=['POST', 'GET'])
def greet():
	name = request.form.get('name_input', 'Guest')

	flash("Hi "+name+", nice to meet you!")

	return render_template('index.html')
