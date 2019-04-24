
"""
W2 Assignment Questions
"""
####################################
####################################
#Q1
####################################

# import data
# sort data by edge length
# working from smallest length edge to biggest, combine clusters until only 4 clusters remain
# relabel edges to reflect the name of the leader nodes
# delete all self referencing edges
# take the minimum length edge and that is the max distance


file = open('W2_Data_Q1_Clustering.txt', 'r')
data1 = file.readlines()
data2 = [line.split() for line in data1]
data2.pop(0)  # removing the total number of nodes, only edges remain
edges = [[int(line[0]), int(line[1]), int(line[2])] for line in data2]  # edges is a list of lists. Small list is 1 edge [node1, node2, length]
edges.sort(key=lambda x: x[2])  # sorting edges by length


###### data structures
# leaders is a dictionary with key = leader of the cluster, value = size
leaders = dict()
for edge in edges:
    leaders[edge[0]] = 1
    leaders[edge[1]] = 1

# clusters is a dictionary with key = leader of the cluster, value = set of nodes in cluster
clusters = dict()
for node in leaders:
    clusters[node] = set([node])

# leader_board is a dict with key= node , value = leader of cluster
leader_board = dict()
for node in leaders:
    leader_board[node] = node

for node in clusters:
    if node not in leader_board:
        print("bruh")


for edge in edges:
    if edge[0] == edge[1]:
        print("asdasasdas", edge)

print("asdasdajdhfajhdbfajhdbfjahbdfjhabdfjhbadjhfb")


def q1_merge(c1, c2):
    """
    :param c1: node
    :param c2: node
    :return: merges the clusters of node1 and node2. Updates the values in leader_board to all point to the same leader.
    The leader is chosen by comparing the size of node1 and node2 clusters.
    """
    global leaders, clusters, leader_board
    sc = c1
    bc = c2
    if leaders[c1] > leaders[c2]:
        sc = c2
        bc = c1

    for node in clusters[sc]:
        leader_board[node] = bc

    leaders[bc] += leaders[sc]
    del leaders[sc]
    clusters[bc] = clusters[bc] | clusters[sc]
    del clusters[sc]


# the algorithm
for edge in edges:
    if len(clusters) == 4:
        break

    if leader_board[edge[0]] != leader_board[edge[1]]:
        q1_merge(leader_board[edge[0]], leader_board[edge[1]])

###########################################

# relabeling the edges
for edge in edges:
    edge[0] = leader_board[edge[0]]
    edge[1] = leader_board[edge[1]]

# removing self referencing edges:
i = 0
while i < len(edges):
    if edges[i][0] == edges[i][1]:
        edges.pop(i)
    else:
        i += 1

print(edges)
#answer is 106




####################################
#Q2
####################################

ZERO = "000000000000000000000000"
#Helper functions
def hamming_dist(node1, node2):
    """
    :param node1: string, of '0' and '1'
    :param node2: string, of '0' and '1'
    :return: integer, the hamming distance between node 1 and node 2
    """
    dist = 0
    for i in range(24):
        if node1[i] != node2[i]:
            dist += 1
    return dist


def clust_merge(score1, node1, score2, node2):
    """
    :param score1: the centered score of node 1
    :param node1: a node from cluster 1
    :param score2: the centered score of node 2
    :param node2: a node from cluster 2
    :return: nothing. In global variable cn, takes the larger cluster and adds all the nodes from the smaller then
    deletes the smaller. In global variable sni, changes the pointers of the nodes in the smaller cluster to point to the
    larger cluster
    """
    global sni, csn, csize

    #determine the smaller and bigger cluster
    scluster = sni[score1][node1]
    bcluster = sni[score2][node2]
    if csize[scluster] > csize[bcluster]:
        scluster = sni[score2][node2]
        bcluster = sni[score1][node1]

    #update big cluster's size
    csize[bcluster] += csize[scluster]
    del csize[scluster]

    for score in csn[scluster]:
        #updating the pointer in sni
        for node in csn[scluster][score]:
            sni[score][node] = bcluster

        #merging the clusters together in csn
        if score in csn[bcluster]:
            csn[bcluster][score] = csn[bcluster][score] | csn[scluster][score]
        else:
            csn[bcluster][score] = csn[scluster][score]

    #delelting the smaller cluster
    del csn[scluster]


#####
#Data processing 1
#after this step, graph should be a list of strings that are made up of '0' and '1'
file = open('W2_Data_Q2_Clustering_Big.txt', 'r')
q2_data = file.readlines()
q2_graph_info = q2_data.pop(0)
q2_graph = []

for line in q2_data:
    node = ""
    for i in range(0, 47, 2):
        if '0' == line[i] or '1' == line[i]:
            a = line[i]
            node += a

    q2_graph += [node]
q2_graph = list(set(q2_graph))

#Data processing 2
#calculate score of nodes relative to the ZERO node. Scored nodes will be a list of lists. smallest list -> [score, node]
scored_nodes = []
for node in q2_graph:
    score = hamming_dist(ZERO, node)
    scored_nodes += [[score, node, None]]
scored_nodes.sort(key=lambda x: x[0])
#####


#Data Structures:

# sni (score node id) will be a dict of dict. key1 = centered score, key2 = node, value = cluster id of the node
sni = dict()
for i in range(2, 23):
    sni[i] = dict()

#csn (cluster score node ) will be a dict with key1 = cluster id, key2 = score,  value = set of nodes
csn = dict()

cluster_id_count = 0
csize = dict()

####The algorithm
for i in range(len(scored_nodes)):
    # make a cluster for the node
    score = scored_nodes[i][0]
    node = scored_nodes[i][1]
    csn[cluster_id_count] = dict()
    csn[cluster_id_count][score] = set([node])
    sni[score][node] = cluster_id_count
    last_cluster = cluster_id_count
    csize[cluster_id_count] = 1
    cluster_id_count += 1

    # compare it to other clusters
    boost = 0
    while boost > -3:

        if score + boost not in sni:
            break

        for node2 in sni[score + boost]:
            if sni[score + boost][node2] == last_cluster:
                pass
            elif hamming_dist(node, node2) < 3:
                clust_merge(score, node, score + boost,  node2)
                last_cluster = sni[score + boost][node2]

        boost -= 1

#############################################
print(len(csn))

#Answer for q2 is 6118
#run time was about 5.5 hours
#code above is not optimized for the problem; only need to address pointers for nodes within 2 socres
