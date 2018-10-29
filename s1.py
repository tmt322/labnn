#Name: Triet Truong
#Email: tmt322
#Assignment: lab 5 - Python Q1
#Date: 10/28/2018
#Programming in Python Q1



#Open file by line
openFile = open('students.csv', 'r');
line = openFile.readline()
averageList = [];
nameList = []
#Loop through each line of the file
while line:
	#Store each name/score in a "words" array
	words = line.split(",");
	average = 0;
	nScores = 0;
	#Loop through each word/number in a line
	for i in words:
		#Check if each element of the "words" array is a name or a score
		try:
			#Convert the scores to integer and add them up
			#Also check for the number of scores for each person
			i = int(i);
			average += i;
			nScores += 1;
		except ValueError:
			name = i;
	#Calculate average by taking total score divided by number of scores
	average = float(average)/nScores;
	averageList.append(average);
	nameList.append(name);
	#Open the next line
	line = openFile.readline();

#Print into two columns
for item1, item2 in zip(nameList, averageList):
	print "%-10s %.2f" % (item1, item2);
