from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/user/<name>/')
def hello_user(name):
	return 'Hello User! ' + str(name)

@app.route('/admin/<name>/')
def hello_admin(name):
	return 'Hello Admin! ' + str(name)

@app.route('/guest/<name>/')
def hello_guest(name):
	if name == 'admin':
		return redirect(url_for('hello_admin',name = name))
	elif name == 'user':
		return redirect(url_for('hello_user',name = name))
	else:
		return 'Hello Guest %s' % name

#APIs to understand getting values from HTML form
@app.route('/success/<name>/')
def success(name):
	return 'Welcome %s' % name

@app.route('/login',methods = ['POST','GET'])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success',name = user))

#Decorator to add URL Rules
#app.add_url_rule('/hello/<name>','hello',hello_world)

if __name__== '__main__':
	app.debug = True
	#app.run(host='0.0.0.0') #For external clients to access this server
	app.run()
	app.run(debug = True)