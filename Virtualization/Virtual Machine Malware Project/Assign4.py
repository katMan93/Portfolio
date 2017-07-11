# This Python program simply analyzes the results of
#  scoreTracker.txt and outputs a verdict whether or not it
#  is running in a virtual machine

lineCount = 0
numMatches = 0
maxNumMatches = 7

scoreFile = open("./scoreTracker.txt",'r')
while lineCount < maxNumMatches:
    line = scoreFile.readline()
    line = line.rstrip('\n')
    if line != '0':
        numMatches = numMatches + 1
    lineCount = lineCount + 1

if numMatches >= maxNumMatches * 0.6:
    print "VMware virtual machine detected."
else:
    print "No VMware virtual machine detected"
