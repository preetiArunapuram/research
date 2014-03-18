import csv
import re
from itertools import izip

#Pulls out preliminary information about the questions, owners, creation dates, etc., and stores information into a csv file
def extractInfo(inputfile, outputfile):
	iFile = open(inputfile,'rb')
	with open(outputfile,'wb') as output:
		#reader = csv.reader(i,delimiter=',')
		writer = csv.writer(output,lineterminator='\n')

		for line in iFile:
			idIndex = line.find('ID')
			creationIndex = line.find('CreationDate')
			ownerIndex = line.find('Owner')
			acceptedAnswerIndex = line.find('AcceptedAnswer')
			tagIndex = line.find('Tags')
			titleIndex = line.find('Title')

			idLine = line[idIndex+3:]
			creationLine = line[creationIndex+13:]
			ownerLine = line[ownerIndex+6:]
			acceptedAnswerLine = line[acceptedAnswerIndex+15:]
			tagLine = line[tagIndex+5:]
			titleLine = line[titleIndex+6:]
			#print idLine

			idList = idLine.split('\t')
			creationList = creationLine.split('\t')
			ownerList = ownerLine.split('\t')
			acceptedAnswerList = acceptedAnswerLine.split('\t')
			tagList = tagLine.split('\t')
			title = titleLine[0:len(titleLine)-2]

			#print idList

			id = idList[0]
			creationDate = creationList[0]
			ownerDate = ownerList[0]
			acceptedAnswer = acceptedAnswerList[0]
			allTags = tagList[0]
			titleLengthChar = len(title)
			titleLengthWords = len(title.split(' '))

			writer.writerow([id,creationDate,ownerDate,acceptedAnswer,allTags,title,titleLengthChar,titleLengthWords])

#Parses tags from original form and returns a list of tag strings
def parseTags(tagString):
	tagsList = re.findall(r"[\w']+",tagString)
	return tagsList

#Combine the accepted answer elapsed times and earliest answer elapsed times for all appropriate questions
def combineTimes(acceptedTimeFile, earliestTimeFile, outputFile):
	with open(acceptedTimeFile,'rb') as aF, open(earliestTimeFile,'rb') as eF, open(outputFile,'wb') as output:
		acceptedReader = csv.reader(aF,delimiter=',')
		earliestReader = csv.reader(eF,delimiter=',')
		writer = csv.writer(output,lineterminator='\n')

		for line1,line2 in izip(acceptedReader,earliestReader):
			id1 = line1[0]
			id2 = line2[0]
			#print id1,id2

			while not id1 == id2:

				if id1 > id2:
					line2 = earliestReader.next()

				elif id2 > id1:
					line1 = acceptedReader.next()

				id1 = line1[0]
				id2 = line2[0]
				#print id1,id2	
			#print id1

			accepted = line1[1]
			earliest = line2[1]

			writer.writerow([id1,accepted,earliest])

def combineAll(initialFile, timeFile, outputFile):
	with open(initialFile,'rb') as initials, open(timeFile,'rb') as times, open(outputFile,'wb') as output:
		initialReader = csv.reader(initials,delimiter=',')
		timeReader = csv.reader(times,delimiter=',')
		writer = csv.writer(output,lineterminator='\n')

		for line1,line2 in izip(initialReader,timeReader):
			id1 = line1[0]
			id2 = line2[0]
			#print id1,id2


			while not id1 == id2:
				if id1 > id2:
					line2 = timeReader.next()

				elif id2 > id1:
					line1 = initialReader.next()

				id1 = line1[0]
				id2 = line2[0]

			#print id1,id2
			row = line2 + line1[1:len(line1)]
			#print row

			writer.writerow(row)



extractInfo("full data/questions.txt","full data/initialExtraction.csv")
combineTimes("full data/Elapsed/question accepted answer time_sorted.csv", "full data/Elapsed/question earliest answer time.csv","full data/Elapsed/question all answer times.csv")
combineAll("full data/initialExtraction.csv","full data/Elapsed/question all answer times.csv","full data/fullData.csv")