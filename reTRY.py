import re, sys, nltk, time
import nameGen, getText, getDocList

parameterFile = sys.argv[-1]

paramF = open(parameterFile, 'r')
header = paramF.readline().strip()
path = paramF.readline().strip().split(" ")[2]
startNo = int(paramF.readline().strip().split(" ")[2])
endNo = int(paramF.readline().strip().split(" ")[2])
ext = paramF.readline().strip().split(" ")[2]
baseName = paramF.readline().strip().split(" ")[2]
res_Path = paramF.readline().strip().split(" ")[2]
res_BaseName = paramF.readline().strip().split(" ")[2]
res_Extension = paramF.readline().strip().split(" ")[2]

for currentNo in range(startNo, endNo+1):
	fileName =  nameGen.getVar(path, baseName, currentNo, ext)

	with open (fileName, "r") as myfile:
	    s=myfile.read()

	first, last = 0, 0

	resFileName = nameGen.getVar(res_Path, res_BaseName, currentNo, res_Extension)
	resultFile = open(resFileName, "w+")

	#get first and last match position
	length = 0

	#TRIAL STRING
	#s = "(i) This is the first of 4 statements \n (ii) This is the second statement! .... \n (iii) Final statement, did you gotcha? (iv)aaa"
	# ALL FIT : ^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$

	# Get list of violations
	splitText = getText.getText(s)
	tic = time.time()
	for resString in splitText:
		# For each violation	
		# We get all text b/w two roman numerals, without new lines
		resString = resString.replace("\n", "")

		# Clear string of all stop words, then rejoin string
		resString = re.split("\s+", resString)
		resString = [w for w in resString if not w in nltk.corpus.stopwords.words('english')]
		resString = " ".join(resString)
		
		# Clear all . , - ' " and other stuff
		pat = re.compile(r"([^\w\.])", re.I)
		for _ in pat.finditer(resString):
			resString = resString.replace(_.group(), " ")
		'''
		pat = re.compile(r"[\d-]", re.I)
		for _ in pat.finditer(resString):
			resString = resString.replace(_.group(), " ")
		'''
		# string is now ready for extraction
		print "AXXXB", resString, "MMMM"

		'''Final file with all violations, stopwords, punctuations removed'''
		resultFile.write("\n"+str(resString)+"\n")
	toc = time.time()

	print "Time taken : ", toc-tic, " sec."

	resultFile.close()