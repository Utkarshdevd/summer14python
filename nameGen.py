import sys

def getVar(path, baseName, currentNo, ext):
	string = path+str(baseName)+str(currentNo)+"."+ext
	return string

def loopStart(path, baseName, startNo, endNo, ext):
	for currentNo in range(startNo, endNo):
		res = getVar(path, baseName, currentNo, ext)
		return res

def main():
	path = sys.argv[1]
	baseName = sys.argv[2]
	startNo = sys.argv[3]
	endNo = sys.argv[4]
	ext = sys.argv[5]

	print loopStart(path, baseName, startNo, endNo, ext)

	print path, baseName, startNo, endNo, ext