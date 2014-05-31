import re
import sys

fileName = sys.argv[-1]


with open (fileName, "r") as myfile:
    s=myfile.read().replace('\n', '')



c,e = 0,0

#s = "(i) This is the first of 4 statements \n (ii) This is the second statement! .... \n (iii) Final statement, did you gotcha? (iv)aaa"
# ALL FIT : ^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
pattern = re.compile(r"\((xc|xl|l?x{0,3})(ix|iv|v?i{0,3})\)")

#get first match!!

iteratable = pattern.finditer(s)

#get first match position
for m in iteratable:
	c = m.start()
	#e = m.end()
	break

#get length of iterator
length = sum(1 for _ in iteratable)	

count  = 0
#Extract all between two consecutive roman numerals
for m in pattern.finditer(s):
	print count, length
	if(c!=m.start()):
		if(count > length-1):
			print "c",s[c+e:m.start()].replace(m.group(), "!!!!")
			print "a",s[m.start()+e:].replace(m.group(), "!!!!")
		else:
			print "b",s[c+e:m.start()].replace(m.group(), "!!!!")
			c = m.start()
			#e = m.end()
	count += 1