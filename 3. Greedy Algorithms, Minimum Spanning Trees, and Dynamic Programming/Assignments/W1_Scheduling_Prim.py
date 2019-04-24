"""
Week 1 assignment including task scheduling (Q1 and Q2) and Prim's Algorithm for MSTs (Q3)
"""


####################################
# importing data

#Jobs data
file = open('W1_data_jobs.txt', 'r')
data = file.readlines()
file.close()
num_jobs = data.pop(0)
# format is [job1, job2, etc] where each job is a list of ints: (weight, length).
jobs = [[int(job.split()[0]), int(job.split()[1])] for job in data]

#edge data
file = open('W1_data_edges.txt', 'r')
data = file.readlines()
file.close()
graph_info = data.pop(0)
num_nodes = graph_info.split()[0]
num_edges = graph_info.split()[1]
edges = [[int(edge.split()[0]), int(edge.split()[1]), int(edge.split()[2])] for edge in data] #vertice1, vertice2, length


####################################
# Q1
# Creating a schedule using (weight - length) values and ordering jobs in decreasing order


q1_sched = []
q1_wct = 0
q1_time = 0
wml_values = [job[0] - job[1] for job in jobs] # all the weight - length (wml) value
jobs_wml = dict() #key = wml value, value = list of all jobs with that wml (this is a list of lists)


# filling jobs_wml appropriately 
for job in jobs:
    if job[0] - job[1] not in jobs_wml:
        jobs_wml[job[0] - job[1]] = []
    jobs_wml[job[0] - job[1]] += [job]

# sorting each value of jobs wml so that jobs with high weight will be at the front of the list
for wml in jobs_wml:
    jobs_wml[wml].sort(key=lambda x: x[0], reverse=True)

# sorting the criteria values to be descending
wml_values.sort(reverse=True)

# creating the schedule
for wml in wml_values:
    q1_sched += [jobs_wml[wml].pop(0)]


# Calculating the weighted completion time
for job in q1_sched:
    weight = job[0]
    length = job[1]
    q1_time += length
    q1_wct += weight * q1_time

print("Question 1 weighted completion time:", q1_wct)
#69119377652

####################################
# Q2
# Creating a schedule using weight/length ratio values and ordering jobs in decreasing order

q2_sched = []
q2_wct = 0
q2_time = 0
wlr_values = [job[0]/job[1] for job in jobs]  # all the weight - length (wml) value
jobs_wrl = dict()  # key = wml value, value = list of all jobs with that wml (this is a list of lists)


# filling jobs_wrl appropriately
for job in jobs:
    if job[0] / job[1] not in jobs_wrl:
        jobs_wrl[job[0] / job[1]] = []
    jobs_wrl[job[0] / job[1]] += [job]

# sorting ratios to be descending
wlr_values.sort(reverse=True)

# creating the schedule
for wlr in wlr_values:
    q2_sched += [jobs_wrl[wlr].pop(0)]


# Calculating the weighted completion time
for job in q2_sched:
    weight = job[0]
    length = job[1]
    q2_time += length
    q2_wct += weight * q2_time

print("Question 2 weighted completion time:", q2_wct)
# 67311454237



####################################
# Q3
# Prim's Algorithm


graph = dict()
path_nodes = dict()
node_path = dict()
lengths = []
#lengths = [[None, None, None]]
node= 1 #Arbitrarily pick 1 as the starting node
path_sum = 0


for edge in edges:
    if edge[0] not in graph:
        graph[edge[0]] = set([])
    if edge[1] not in graph:
        graph[edge[1]] = set([])
    graph[edge[0]].add((edge[1], edge[2]))
    graph[edge[1]].add((edge[0], edge[2]))

    path_nodes[edge[2]] = set([])

    node_path[edge[0]] = float('inf')
    node_path[edge[1]] = float('inf')

del node_path[node]

while node_path:
    node_connections = graph[node]

    for connection in node_connections:
        # Potentially replacing the shortest path to the destination node
        if connection[0] in node_path:
            if connection[1] < node_path[connection[0]]:
                old_length = node_path[connection[0]]
                node_path[connection[0]] = connection[1]

                if old_length < float('inf'):
                    path_nodes[old_length].remove(connection[0])
                path_nodes[connection[1]].add(connection[0])

                if old_length < float('inf'):
                    lengths.remove(old_length)

                lin_min_insert(lengths, connection[1])


                n = 0
                while n < len(lengths):
                    if connection[1] <= lengths[n]:
                        lengths.insert(n, connection[1])
                        break

                    n += 1

                if len(lengths) == 0 or connection[1] > lengths[-1]:
                    lengths += [connection[1]]


    # Choosing the next node to add
    if len(lengths) > 0:
        next_length = lengths.pop(0)
        node = path_nodes[next_length].pop()
        del node_path[node]
        path_sum += next_length


print("Question 3 path length sum:", path_sum)
#-3612829


visited = set()
graph = graph

def prim(edges):

    edges.sort()
    path_sum = 0
    for edge in edges:
        if edge[0] not in visited or edge[1] not in visited:
            path_sum += edge[2]
            visited.add(edge[0])
            visited.add(edge[1])
