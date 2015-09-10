from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy import Table, Column, String #Integer, Date, Float
# import config 

# app = Flask(__name__)
# app.config = ['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
# db = SQLAlchemy(app)
from main import db

class Alleles(db.Model):
	__tablename__ = "alleles"

	alleleID = db.Column('id', db.Integer, primary_key=True)
	chromosome = db.Column('Chr', db.String, nullable=False)
	Start = db.Column('Start', db.Integer)
	End = db.Column('End', db.Integer)
	Ref = db.Column('Ref', db.String)
	Alt = db.Column('Alt', db.String)
	FuncrefGeene = db.Column('FuncrefGene', db.String)
	GenerefGene = db.Column('GenerefGene', db.String)
	ExonicFuncrefGene = db.Column('ExonicFuncrefGene', db.String)
	AAChangerefGene = db.Column('AAChangerefGene', db.String)
	phastConsElements46way = db.Column('phastConsElements46way', db.String)
	genomicSuperDups = db.Column('genomicSuperDups', db.String)
	snp138 = db.Column('snp138', db.String)
	hum_mus_phastcons_chr = db.Column('hum_mus_phastcons_chr', db.String)
	primates_phastcons_chr = db.Column('primates_phastcons_chr', db.String) 
	hum_mus_vista_chr	= db.Column('hum_mus_vista_chr', db.String)
	indiaFreq = db.Column('indiaFreq', db.String)
	Otherinfo = db.Column('Otherinfo', db.String)

	def __init__(self):
		pass

	def __repr__(self):
		return '<div>Hello World</div>'

