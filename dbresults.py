#@imyjimmy
#the purpose of this file is to provide helper methods
#to manage db results returned from db queries.

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