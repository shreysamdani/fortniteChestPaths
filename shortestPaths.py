import json
import sys
import subprocess

subprocess.Popen("curl -X GET 'http://www.fortnitechests.info/api/markers' -H 'accept: application/json' > chests.json")

with open('chests.json') as f:
    data = json.load(f)
    locations = [d["coordinates"] for d in data if d["type"] == "loot"]

distBetween = lambda x,y: int(((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5)

dist = [[distBetween(i,j) for j in locations] for i in locations]


# https://gist.github.com/snakers4/91fa21b9dda9d055a02ecd23f24fbc3d
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
	"""
	Call in a loop to create terminal progress bar
	@params:
		iteration   - Required  : current iteration (Int)
		total       - Required  : total iterations (Int)
		prefix      - Optional  : prefix string (Str)
		suffix      - Optional  : suffix string (Str)
		decimals    - Optional  : positive number of decimals in percent complete (Int)
		length      - Optional  : character length of bar (Int)
		fill        - Optional  : bar fill character (Str)
	"""
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix),'\r' )
	# Print New Line on Complete
	if iteration == total: 
		print()


V = len(locations)
INF = sys.maxsize

def shortestPath(graph, k):

	distTo = [[[INF] * (k + 1) for _ in range(V)] for _ in range(V)]
	edgeTo = [[[-1] * (k + 1) for _ in range(V)] for _ in range(V)]

	# Loop for number of edges from 0 to k
	for numEdges in range(k + 1):

		for i in range(V):  # for source
			printProgressBar(i, V, str(numEdges + 1) + "/" + str(k + 1))

			for j in range(V): # for destination

				if numEdges == 0 and i == j:
					distTo[i][j][numEdges] = 0

				if numEdges == 1:
					distTo[i][j][numEdges] = graph[i][j]
					edgeTo[j][i][numEdges] = j


				if (numEdges > 1):
					for a in range(V):
						if i != a and j!= a and distTo[a][j][numEdges-1] != INF:
							if graph[i][a] + distTo[a][j][numEdges-1] < distTo[i][j][numEdges]:
								distTo[i][j][numEdges] = graph[i][a] + distTo[a][j][numEdges-1]
								edgeTo[j][i][numEdges] = a

	for i in range(len(edgeTo)):
		printProgressBar(i, V, "writing %s of %s files" % (i, V))
		with open('distances/distance' + str(i), 'w+') as f:
			f.write(str(edgeTo[i]))


shortestPath(dist, 50)
subprocess.Popen("rm chests.json")

