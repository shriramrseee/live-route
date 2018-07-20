import random
import csv

nodes = 50

adj = [[0 for j in range(0,nodes)] for i in range(0,nodes)]

dist = [[0 for j in range(0,nodes)] for i in range(0,nodes)]

#Generating random adjacency matrix  with given average degree per node

degree = 4

for i in range(0,nodes):
    for j in range(i+1,nodes):
        r = random.randint(1,nodes-1)
        if r<=degree:
            adj[i][j] = adj[j][i] = 1

#Generating random distance matrix with given min and max distances

min = 1
max = 10

for i in range(0,nodes):
    for j in range(i+1,nodes):
        if adj[i][j] == 1:
            dist[i][j] = dist[j][i] = random.randint(min, max)

with open('adjacency.csv', 'w') as f:
    w = csv.writer(f)
    for i in range(0,nodes):
        w.writerow(adj[i])

with open('distance.csv', 'w') as f:
    w = csv.writer(f)
    for i in range(0,nodes):
        w.writerow(dist[i])

