import sys, getopt

def buildAlleleDict(file):
	returnDict = {}
	for line in file:
		l = line.split('\t')
		print l
		print len(l)
		if len(l) is 8:
			returnDict[':'.join(l[1:6])] = l[7].strip() 
			print("returnDict key: " + ':'.join(l[1:6]))
	return returnDict

def annotate(filein, fileout, alleleDict): 
	with open(filein, 'r') as input, open(fileout, 'w') as output:
		firstline = input.readline()
		header = firstline.split('\t')
		insertIndex = len(header)-1
		header.insert(insertIndex, 'indiaFreq')

		output.write('\t'.join(header))

		for line in input:
			l = line.split('\t')
			id = ':'.join(l[0:5])
			if id in alleleDict:
				print("match: " + alleleDict[id])
				l.insert(insertIndex, alleleDict[id])
			else:
				print("no match for id: " + id + "... printing N/A")
				l.insert(insertIndex, 'N/A')
			output.write('\t'.join(l))

def main(argv):
	global alleleDict
	global firstline
	input = '' #points to a vcf file
	output = '' #output vcf file

	#hard coded, but can be changed to accept a param
	alleles = 'iafFreq.txt'

	try:
		opts, args = getopt.getopt(argv,'hi:o:', ['input=', 'output='])
	except getopt.GetoptError:
		print 'indiaAlleleAnnotator.py -i <infile> -o <outfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'indiaAlleleAnnotator.py -i <infile> -o <outifle>'
			sys.exit()
		elif opt in ('-i', '--input'):
			input = arg
		elif opt in ('-o', '--output'):
			output = arg
	#print 'input file is ', infile
	#print 'output file is ', outfile
	
	alleleDict = buildAlleleDict(open(alleles, 'r'))

	annotate(input, output, alleleDict)

if __name__ == "__main__":
	main(sys.argv[1:])
