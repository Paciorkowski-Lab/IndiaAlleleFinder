# import sqlite3
from flask import Flask, url_for, request, session, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)
app.secret_key = "my precious"

# app.config.update(SEND_FILE_MAX_AGE_DEFAULT = 240)
#DATABASE = '/Users/imyjimmy/Dropbox/for_alex/indiaAlleleFinder/db/database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jzhang69:' + base64.b64decode("QnIwMGtseW4h") + '@mysql.imyjimmy.com/indiaallelefinderdb'
# app.config.from_object(__name__)

db = SQLAlchemy(app)

import model

def get_db():
	return db

def execute_query(query, args={}):
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

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('search')
	results = processQuery(query)
	# print("results: " + str(results))
	html = makeTable(results)
	# print("html: " + html)
	return render_template('search.html', query=query, results=results, h=html)

def processQuery(query):
	gene_rows = execute_query("SELECT * FROM alleles WHERE GenerefGene=:param", {"param": query})
	return gene_rows

#DOES THE FOLLOWING:
#["(u'1'", " u'14653'", " u'14653'", " u'C'", " u'T'", " u'ncRNA_exonic'", " u'WASH7P'", " u'NA'", " u'NA'", " u'NA'", " u'Score=0.993729;Name=chr9:10843'", " u'rs62635297'", " u'NA'", " u'NA'", " u'NA'", " u'india:0.280487804878'", " u'1')"]
#(u'12', u'53708092', u'53708092', u'A', u'G', u'exonic', u'AAAS', u'synonymous SNV', u'AAAS:NM_001173466:exon6:c.T580C:p.L194L,AAAS:NM_015665:exon7:c.T679C:p.L227L', u'Score=635;Name=lod=508', u'NA', u'rs80027466', u'Name=yes', u'Name=yes', u'NA', u'india:0.020325203252', u'12')
#u'AAAS:NM_001173466:exon6:c.T580C:p.L194L,AAAS:NM_015665:exon7:c.T679C:p.L227L'
# element:
#(u'12
#u'3433
# u'AAAS:NM_001173466:exon6:c.T580C:p.L194L
# element:
# AAAS:NM_015665:exon7:c.T679C:p.L227L'
def makeTable(results):
	#very shady but okay for now.
	#@todo: make this less hacky
	header="Chr	Start	End	Ref	Alt	Func.refGene	Gene.refGene	ExonicFunc.refGene	AAChange.refGene	phastConsElements46way	genomicSuperDups	snp138	hum_mus_phastcons_chr	primates_phastcons_chr	hum_mus_vista_chr	indiaFreq	Otherinfo".split('\t')
	#^ that thing is an array. sry guys

	result = {}
	ind = 0
	for column in results:
		result[ind] = []
		# print "hereereee"
		elements = str(column).split("', ")
		print column
		for e in elements:
		 	result[ind].append(str(e).split("u'")[1].split("')")[0])
		ind += 1

	print "result" 
	print result
	compiledStr = "<table class='table table-striped table-condensed'><tbody>"

	compiledStr += "<thead><tr>"
	for thing in header:
		compiledStr += "<td class='cell'>" + thing + "</td>"
	compiledStr += "</tr></thead>"

	for i in range(0, ind):
		compiledStr += '<tr>'
		for r in result[i]:
			compiledStr += "<td class='cell'>" + r + "</td>"
		compiledStr += '</tr>'
	compiledStr += '</tbody></table>'
	# return '<br>'.join(str(row).split(',') for row in results)
	print compiledStr
	return compiledStr
	
###THE FOLLOWING IS EXAMPLE CODE###
# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello(name=None):
#	return "Hello World!"
# 	return render_template('hello.html', name=name)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	if request.method == 'POST':
# 		return do_the_login()
# 	else:
# 		return show_login_form()

# def do_the_login():
# 	return "login url"

# def show_login_form():
# 	return "login form url"

# @app.route('/user/<username>')
# def showUserProfile(username):
# 	return 'User: ' + username

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

