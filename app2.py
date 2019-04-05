from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')
 
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('template2.html',name=name)

@app.route("/cadastro")
def cadastro():
	return render_template('cadastro.html')
 
if __name__ == "__main__":
	app.run(port=8001)