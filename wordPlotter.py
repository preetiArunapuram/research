import csv
from matplotlib import pyplot as plt

def plotTitles(file,color):
	titleLengths = []
	times = []

	folder = "full_data/tag counts earliest by word/"
	with open(folder+file,'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for line in reader:
			titleLengths.append(line[1])
			times.append(line[2])


	fileString = file.split(".")
	plt.plot(titleLengths,times,color,alpha=0.5)
	plt.title("Question to Earliest Answer Elapsed Time By Title Length By Tag: " + fileString[0])
	plt.ylabel("Elapsed Time in Milliseconds")
	plt.xlabel("Length of Post Title in Characters")
	plt.grid(True)
	#plt.show()

#plotTitles("c#.csv",'ro')
#plotTitles("java.csv",'bo')
#plotTitles("php.csv", 'ro')
plotTitles("javascript.csv", 'go')
#plotTitles("work.csv", 'mo')
plt.show()