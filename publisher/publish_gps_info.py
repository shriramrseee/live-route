from google.cloud import pubsub
import time
import random
import csv
from argparse import ArgumentParser

# Get Command Line arguments
p = ArgumentParser()
p.add_argument('-p', '--project', dest='project_id', default='live-route-210611', help='Project ID')
p.add_argument('-d', '--delay', dest='delay', default=5, help='Time delay between messages in seconds')
p.add_argument('-min', '--minimum', dest='min_speed', default=1, help='Minimum speed')
p.add_argument('-max', '--maximum', dest='max_speed', default=100, help='Maximum speed')
p.add_argument('-g', '--graph', dest='adjacency_file', default='adjacency.csv', help='File path to adjacency mat. csv')
args = p.parse_args().__dict__

# Initialize Publisher
client = pubsub.PublisherClient()
topic_path = client.topic_path(args['project_id'], 'gps-stream')

# Read the graph
with open(args['adjacency_file'], 'r') as f:
    reader = csv.reader(f)
    adj = list(reader)

# Get the list of edges
inc = []

for i in range(0, len(adj[0])):
    for j in range(i, len(adj[0])):
        if adj[i][j] == '1':
            inc.append((str(i), str(j)))

edges = len(inc)

# Publish Random speed for random edge with a given time delay
data = 'GPS Info'

while True:
    random_edge = inc[random.randint(0, edges - 1)]
    client.publish(topic_path, data=data.encode('utf-8'), start_node=random_edge[0], end_node=random_edge[1],
                   speed=str(random.randint(int(args['min_speed']), int(args['max_speed']))))
    time.sleep(int(args['delay']))
