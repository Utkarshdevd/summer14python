import sys, time, nltk
import nameGen

'''Get Parameter File data'''
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

'''Initalize Dictionary'''
dictionaryFile = sys.argv[-2]
# Get vocabulary
with open(dictionaryFile, "r") as myfile:
		vocab = myfile.read()
vocab = vocab.split()

# Clear string of all stop words, then rejoin string
resString = re.split("\s+", resString)
resString = [w for w in resString if not w in nltk.corpus.stopwords.words('english')]
resString = " ".join(resString)

'''Weed out words found in vocabulary and add new words to it'''
res = []
'''
Attempt idiomatic version, this one cannot update vocab at the same time, hence has redundant words
but is faster than the other approach
res = [word for word in data if not word in vocab]
'''
tic = time.time()
flag = True
for currentNo in range(startNo, endNo+1):
	# Get file name
	fileName = nameGen.getVar(res_Path, res_BaseName, currentNo, res_Extension)
	# Get file data
	with open(fileName, "r") as myfile:
	    data = myfile.read()

	data = data.split()
	for word in data:
		for v in vocab:
			if v == word:
				flag = False

		if flag:
			vocab.append(word)
			res.append(word)
		flag = True
toc = time.time()
print "Time taken : ", toc-tic, " sec."

dictName = "newDict.txt"

with open(dictName, "w+") as myfile:
	for word in res:
		myfile.write(str(word)+"\n")
