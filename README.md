# Fortnite Chest Paths
Runs an extended version of Floyd-Warshall's algorithm to find the shortest path between chests in Fortnite while accessing a certain number of chests.

chest information from http://www.fortnitechests.info/  
base algorithm from https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph/


## Setup
 - make sure Python 3 is installed
 - run ```python3 shortestPaths.py``` to generate the shortest paths from the chest data
 - run ```pip3 install flask``` to make sure the Flask library is installed
 - run ```env FLASK_APP=chestsBackend.py flask run``` to start the backend server
 - open chestMap.html
