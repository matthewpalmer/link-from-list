#file to be written to
f = open('/Users/Matthew/python/thrashing/listfile.txt', 'r+')
#file to be read from. Links must be on a new line
g = open('/Users/Matthew/python/thrashing/resources.txt','r')
myArray = []
print "some new change that doesn't do anything"

for line in g:
    myArray.append(line),

f.read()
print f.read()
for line in f:
    print line

newlist = []
for w in myArray:
    newStr = "<a href='"+w+"'>"+w+"</a>"
    newlist.append(newStr)
list(enumerate(myArray))
print newlist
for e in newlist:
    f.write(e+'\n')
