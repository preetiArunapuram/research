import csv
import operator

def sort_table(table, col=0,reverseVal=False):
	return sorted(table, key=operator.itemgetter(col),reverse=reverseVal)
	#table.sort(key=lambda k: k[col], reverse=True)

def sort(file, sortedFileName,sortColumn,reverseVal=False):
	itemList = []
	with open(file, 'rb') as csvfile:
		d = csv.reader(csvfile, delimiter=',')
		for line in d:
			itemList.append([line[0],int(line[sortColumn])])
	sortedList = sort_table(itemList,sortColumn,reverseVal)
	#print sortedTagList
	
	with open(sortedFileName, 'wb') as csvfile:
		#d = csv.DictWriter(csvfile, ['Word', 'Question Count'])
		#d.writeheader()
		writer = csv.writer(csvfile, lineterminator='\n')
		writer.writerows(sortedList)
		
#sort("full_data/word question counts.csv", "full_data/word_question_counts_sorted.csv")
#sort("full_data/ElapsedTimes/owner earliest answer times.csv","full_data/ElapsedTimes/owner_earliest_answer_times_sorted.csv")
#sort("full_data/owner question counts.csv","full_data/owner_question_counts_sorted.csv")
#sort("full_data/quest_allAnswers.csv","full_data/question_allAnswers_sorted.csv")	
#sort("full data/Elapsed/question accepted answer time.csv","full data/Elapsed/question accepted answer time_sorted.csv")
sort("full data/tag question counts.csv","full data/tag_question_counts_sorted.csv",1,True)