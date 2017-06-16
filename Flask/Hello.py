from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

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

#APIs to use HTML rendering from Python code
@app.route('/hardhtml/')
def render_html():
	return '<html><body><h1>I am HTML Renderered from Python</h1></body></html>'

@app.route('/templatehtml/')
def template_html():
	return render_template('first_hello.html')

@app.route('/usertemplate/<user>/')
def user_html(user):
	return render_template('first_hello.html',name = user)

@app.route('/mongo/')
def mongo_test():
	client = MongoClient() #default localhost 27017
	pass_html = list()
	db = client['database_ui1']
	posts = db.posts
	strId = "[" + "STATUS_MESSAGE_WILL_BE_DELETED_24_HOURS" + "]"
	string_posts = posts.find({},{strId:1,'File':1})

	print string_posts

	for i in string_posts:
		if strId in i:
			pass_html.append(i)
	print pass_html
	return render_template('condition.html', result = pass_html)


#Decorator to add URL Rules
#app.add_url_rule('/hello/<name>','hello',hello_world)

if __name__== '__main__':
	app.debug = True
	#app.run(host='0.0.0.0') #For external clients to access this server
	app.run()
	app.run(debug = True)
