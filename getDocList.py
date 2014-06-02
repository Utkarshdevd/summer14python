import sys
import nameGen

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

def getDocs():
	docs = []
	for currentNo in range(startNo, endNo+1):
		fileName = nameGen.getVar(res_Path, res_BaseName, currentNo, res_Extension)

		with open(fileName, "r") as myFile:
			data = myFile.read()

		docs.append(data)

	return docs