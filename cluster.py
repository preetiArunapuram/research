import csv
from itertools import izip
import extractInfo

firstPronoun = ['i', 'mine', 'my', 'myself',"i'll", 'we', "we'll","we've","i've","i'm","we're","our", "ours","ourselves","ourself","us","i'd","we'd"]
secondPronoun = ["you","your","yours","you've","you'll","you're","yourself","yourselves","you'd"]
thirdPronoun = ["he","she","he","her","his","hers","himself","hisself","herself","he'll","she'll","he's","she's","they","they'll","they're","their","they've","themself","themselves","he'd","she'd","they'd"]

punctuation = ['.','?','!',':','~',';','(',')','<','>']
negation = ['not','null','nil','none','nothing','never',"won't","shouldn't","wouldn't"]
politeness = ['please', 'thank','thanks','could',"help","appreciate","grateful","much","appreciated","help","helped"]

def getTopTags(inputFile,outputFile):
	with open(inputFile,'rb') as iFile, open(outputFile,'wb') as output:
		reader = csv.reader(iFile,delimiter=',')
		for i in range(0,100):
			line = reader.next()
			tag = line[0]

			output.write("%s\n" % tag)


def storeTagPositions(topTags):
	count = 0
	d = {}

	with open(topTags,'rb') as tags:
		for line in tags:
			#print line
			d[line[0:len(line)-1]] = count
			count += 1
	return d

def trackAllGroups(inputfile,textColumn,tagColumn,outputfile):
	with open(inputfile,'rb') as iFile, open(outputfile,'wb') as output:
		reader = csv.reader(iFile,delimiter=',')
		writer = csv.writer(output,lineterminator='\n')

		for line in reader:
			title = line[textColumn]
			binClass = [0,0,0,0,0,0]
			tagPos = [0 for i in range(0,100)]
			#print tagPos

			for word in firstPronoun: 
				if not title.lower().find(" " + word + " ") == -1: binClass[0] = 1

			for word in secondPronoun: 
				if not title.lower().find(" " + word + " ") == -1: binClass[0] = 1

			for word in thirdPronoun: 
				if not title.lower().find(" " + word + " ") == -1: binClass[0] = 1

			for word in punctuation: 
				if not title.lower().find(word) == -1: binClass[0] = 1

			for word in negation: 
				if not title.lower().find(" " + word + " ") == -1: binClass[0] = 1

			for word in politeness: 
				if not title.lower().find(" " + word + " ") == -1: binClass[0] = 1

			tagString = line[tagColumn]
			tagList = extractInfo.parseTags(tagString)
			#print tagList

			for word in tagList:
				if word in d.keys(): 
					#print d[word]
					tagPos[d[word]] = 1

			writer.writerow(line + binClass + tagPos)

			
getTopTags("full data/tag_question_counts_sorted.csv","full data/topTags.txt")			
d = storeTagPositions("full data/topTags.txt")
#print d
trackAllGroups("full data/fullData.csv",7,6,"full data/pronounClusteredData.csv")
