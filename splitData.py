import csv
import os

def getTimesFromCSV(f):
	timesList = []
	with open(f, 'rb') as csvfile:
		listReader = csv.reader(csvfile, delimiter=',')
		for line in listReader:
			timesList.append(int(line[1]))
	return timesList
	
def writeTimesToText(timesList,file):
	with open(file,'wb') as textFile:
		for element in timesList:	
			textFile.write("%d\n" % element)
			
file = "full_data/ElapsedTimes/question accepted answer time.csv"
timesList = getTimesFromCSV(file)
writeTimesToText(timesList, "full_data/accepted_answer_times.txt")

