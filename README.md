# Fortnite Chest Paths
Runs an extended version of Floyd-Warshall's algorithm to find the shortest path between chests in Fortnite while accessing a certain number of chests.

## How it works
 1. The location of the chests are retrieved from link below and made into a graph
 2. The shortest paths from every chest to every other chest is computed using Floyd-Warshal's algorithm
    - A modification (shown by the algorithm below) is made to the dynamic programming algorithm to keep track of the shortest path length using _n_ chests (the modification is another dimension to the DP matrix)
    - I added a second modification to recreate the actual paths
 3. The resulting matrix (used for quick path reconstruction) is stored over a series of files
 4. When two chests are clicked on the frontend, the backend uses those two chests and the DP matrix to find the shortest path and return it to the frontend
 
chest information from http://www.fortnitechests.info/  
base algorithm from https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph/


## Setup
 - make sure Python 3 is installed
 - run ```python3 shortestPaths.py``` to generate the shortest paths from the chest data
 - run ```pip3 install flask``` to make sure the Flask library is installed
 - run ```env FLASK_APP=chestsBackend.py flask run``` to start the backend server
 - open chestMap.html
