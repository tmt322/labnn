#Name: Triet Truong
#Email: tmt322@drexel.edu
#Date: 10/28/18
#Assignment: Python lab Q2

import sys;
#Take the first argument as the file name. If there is none, take stdin as the file
if len(sys.argv == 1):
	filename = sys.argv[1];
	openFile = open(filename, "r");
else:
	filename = sys.stdin;

line = openFile.readline();
#Create an associative array for ids and names
idDict = dict();
while line:
	line = line.strip('\n');
	#Split each record into its id and name
	recordArray = line.split(' ', 1);
	#Add a pair of key and value to the associative array
	idDict[recordArray[0]] = recordArray[1];
	line = openFile.readline();
#Print the id number and name in two columns
for id in sorted(idDict.keys()):
	print ("%-9s %s" % (id, idDict[id]));
