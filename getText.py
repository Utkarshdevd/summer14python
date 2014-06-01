import re

def getText(data):
	res = []
	resString = ""

	pattern = re.compile(r"\(?M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\)(.*?)\. *\n", re.I)
	iteratable = pattern.finditer(data)
	newPattern = re.compile(r"\(?M{0,4}CM|CD|D?C{0,3}XC|XL|L?X{0,3}IX|IV|V?I{0,3}\)", re.I)
	checkPattern = re.compile(r"\(?M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\) *", re.I)
	resString = ""
	for _ in iteratable:
		resString = str(_.group())
		if(newPattern.match(resString) == None):
			for a in checkPattern.finditer(resString):
				resString = resString.replace(a.group(), "")
			res.append(resString)
		else:
			print "notCool"
			continue
	return res