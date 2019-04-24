#Pre-processing step for W2 assignment data: remove all nodes unreachable from node "1".
file = open('W2_Original_File_dijkstraData.txt', 'r')
data = file.readlines()
file.close()
graph_head_key = dict()
graph_length_key = dict()

for line in data:
    tail_paths = line.split()
    tail = tail_paths.pop(0)
    graph_head_key[tail] = dict()
    graph_length_key[tail] = dict()

    for path in tail_paths:
        head = path.split(",")[0]
        length = int(path.split(",")[1])

        graph_head_key[tail][head] = length

        if length not in graph_length_key[tail]:
            graph_length_key[tail][length] = set([])
        graph_length_key[tail][length].add(head)





#############################################################################################################
#############################################################################################################
#This next section is to deteremin


universe = set([])  # set of nodes where that have been determined to be connected to node "1"
universe.add("1")

def universe_add(graph_head_key, source):
    """
    :param graph_head_key:
    :return: the nodes that can be travelled to from the source node
    """

    global universe

    for head in graph_head_key[source]:
        if head in universe:
            continue

        universe.add(head)
        universe_add(graph_head_key, head)


universe_add(graph_head_key, "1")



file = open("W2_Source_Node_Universe.txt", "w")
for node in universe:
    file.write(node + " ")
    sum += 1
file.close()



