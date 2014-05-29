import re
import sys

fileName = sys.argv[-1]


with open (fileName, "r") as myfile:
    s=myfile.read()

first, last = 0, 0

resultFile = open("res.txt", "w")

#get first and last match position
length = 0
'''
pattern = re.compile(r"(\.\n)")
iteratable = pattern.finditer(s)

for m in iteratable:
	if(length == 0):
		first = m.end()
	else:
		print "AAA", s[first:m.end()], "$$$", length
		first = m.end()
	last = m.start()
	print "----------------------------------------------------", m.start(), first
	length += 1
'''
#TRIAL STRING
#s = "(i) This is the first of 4 statements \n (ii) This is the second statement! .... \n (iii) Final statement, did you gotcha? (iv)aaa"
# ALL FIT : ^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
pattern = re.compile(r"\(?M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\)(.*?)\. *\n", re.I)
iteratable = pattern.finditer(s)

#get length of iterator

'''for _ in iteratable:
	if(length == 0):
		first = _.start()
	length += 1
'''
count  = 0
check = ""
#Extract all between two consecutive roman numerals
'''for _ in iteratable:
		if(first != _.start()):
		if(count >= length-1):
			print "AAA"
			print "AXA",s[first:_.start()].replace(check, "!!!!")
			print "AXXB",s[_.start():last].replace(check, "!!!!")
		else:
			print "AXXXB",s[first:_.start()].replace(check, "!!!!")
			first = _.start()
			check = _.group()
	count += 1
'''

#returns None if match found
newPattern = re.compile(r"\(?M{0,4}CM|CD|D?C{0,3}XC|XL|L?X{0,3}IX|IV|V?I{0,3}\)")
checkPattern = re.compile(r"^\(?M{0,4}CM|CD|D?C{0,3}XC|XL|L?X{0,3}IX|IV|V?I{0,3}\)")
resString = ""
for _ in iteratable:
	resString = str(_.group())
	if(newPattern.match(resString) == None):
		for a in checkPattern.finditer(resString):
			print a.group()
	else:
		print "notCool"
		continue
	#resString = resString[last:]
	resString = resString.replace("\n", "")
	print "AXXXB", resString, "MMMM"

	resultFile.write("\n"+resString+"\n")

resultFile.close()