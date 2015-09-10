# import sqlite3
from flask import Flask, url_for, request, session, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "my precious"

app.config.update(SEND_FILE_MAX_AGE_DEFAULT = 240)
#DATABASE = '/Users/imyjimmy/Dropbox/for_alex/indiaAlleleFinder/db/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/indiaAlleleFinderDB'
# app.config.from_object(__name__)

db = SQLAlchemy(app)

import model
# def connect_to_database():
# 	return sqlite3.connect(app.config['DATABASE'])

#@app.before_request
#def before_request():
#	g.db = connect_db()

def get_db():
	return db

# @app.teardown_appcontext
# def close_connection(exception):
# 	db = getattr(g, '_db', None)
# 	if db is not None:
# 		db.close()

def execute_query(query, args={}):
	# sql lite
	# current = get_db().execute(query, args)
	# rows = current.fetchall()
	# current.close()
	#	current = db.session.query(Alleles).all()
	current = db.session.execute(query, args)

	return current

@app.route('/')
@app.route('/index.html')
def index():
	#return 'Welcome to India Allele Finder'
	return render_template('index.html') #will be the search page

@app.route('/viewdb')
def viewdb():
	rows = execute_query("""SELECT * FROM alleles""")
	return '<br>'.join(str(row) for row in rows)

@app.route('/gene/<gene>')
def sort_by_gene(gene):
	rows = execute_query("SELECT * FROM alleles WHERE GenerefGene=:param", {"param": gene})
	return '<br>'.join(str(row) for row in rows)

@app.route('/chr/<chromosome>')
def sort_by_chr(chromosome):
	rows = execute_query("SELECT * FROM alleles WHERE Chr=:param", {"param": chromosome}) #[chromosome]
	return '<br>'.join(str(row) for row in rows)

@app.route('/search')
def search():
	query = request.args.get('search')
	results = processQuery(query)
	print("results: " + str(results))
	html = '<br>'.join(str(row) for row in results)
	print("html: " + html)
	return render_template('search.html', query=query, results=results, h=html)

def processQuery(query):
	gene_rows = execute_query("SELECT * FROM alleles WHERE GenerefGene=:param", {"param": query})
	# print('in processQuery. length of rows: ' + str(len(gene_rows)))
	# for row in gene_rows:
	#  	print("genes: " + str(row))
	return gene_rows



###THE FOLLOWING IS EXAMPLE CODE###
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
#	return "Hello World!"
	return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return do_the_login()
	else:
		return show_login_form()

def do_the_login():
	return "login url"

def show_login_form():
	return "login form url"

@app.route('/user/<username>')
def showUserProfile(username):
	return 'User: ' + username

# with app.test_request_context():
	# print url_for('index')
	# print url_for('login')
	# print url_for('login', next='/')
	# print url_for('showUserProfile', username='John Doe')

# @app.route('/post/<int:postID>')
# def showPost(postID):
# 	return 'Post %d' % postID

if __name__ == "__main__":
	app.run(debug=True)

