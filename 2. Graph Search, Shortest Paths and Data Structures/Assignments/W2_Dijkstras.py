"""
This script contains an implementation of Dijkstras algorithm without using heaps.
"""

#2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
#2599,2610,2947,2052,2367,2399,2029,2442,2505,3068

file = open('W2_Original_File_dijkstraData.txt', 'r')
#file = open('W2_Test.txt', 'r')
data = file.readlines()
file.close()
graph = dict()

for line in data:
    tail_paths = line.split()
    tail = tail_paths.pop(0)

    graph[tail] = dict()

    for path in tail_paths:
        head = path.split(",")[0]
        length = int(path.split(",")[1])

        graph[tail][head] = length

print(graph)


def dijkstras(graph, source):
    """
    :param graph: Dict of Dict, key: tail node - value: (key: head node - value: length of edge)
    :param source: The node to start travelling from
    :return: Dict, key: destination node - value: path length from source node
    """

    #initialize variables
    numNodes = len(graph)
    shortestPaths = {source:0} #Key: destination node - value: path length
    lastNode = source #this is the node that was added last
    lastNodeInfo = dict() #key: head node connected to last node - Value: edge length
    connections = dict()  # Key: headNode - value: edge length

    while len(shortestPaths) < numNodes:
        #Get last node's heads and their lengths
        for node in graph[lastNode]:
            lastNodeInfo[node] = graph[lastNode][node]

        #Update the connection dictionary with the head nodes and edge lengths
        for headNode in lastNodeInfo:
            if headNode in shortestPaths:
                continue

            if headNode in connections:
                if connections[headNode] > lastNodeInfo[headNode] + shortestPaths[lastNode]:
                    connections[headNode] = lastNodeInfo[headNode] + shortestPaths[lastNode]
            else:
                connections[headNode] = lastNodeInfo[headNode] + shortestPaths[lastNode]

        #add the head with min path length in connections to shortestPaths
        lastNode = min(connections, key=connections.get)
        shortestPaths[lastNode] = connections[lastNode]
        del connections[lastNode]

        lastNodeInfo = dict()


    return shortestPaths




#######################################
#Getting answer distances

d = dijkstras(graph, "1")

ans_nodes = set(["7","37","59","82","99","115","133","165","188","197"])
answer = []
lengths = ""

for node in d:
    if node in ans_nodes:
        answer += [(int(node), d[node])]
answer.sort(key=lambda x: x[0])
print("answer", answer)

for node in answer:
    lengths += str(node[1]) + ","
print("lengths", lengths)

