data = open('W4_adjacency_list_graph.txt', 'r')
graph_text = data.readlines()
graph = {}
nodes = set()
for line in graph_text:
    temp = line.split()
    key = int(temp[0])
    value = list(map(lambda x: int(x), temp[1:]))
    value.sort()

    graph[key] = value
    nodes.add(key)




def approx_min_cut_find(graph, nodes, pick):
    """
    :param graph: Adjacency list graph.
    :param graph: A set of nodes in the graph.
    :return: int representing the number of crossing edges
    """

    a = [set([pick]), graph[pick]]
    b = nodes
    num_nodes = len(nodes)
    low_count = 500

    while len(a[0]) < num_nodes - 1:
        next = max(set(a[1]), key=a[1].count)

        a[0].add(next)

        a[1] = list(filter(lambda x: x != next, a[1]))

        for edge in graph[next]:
            if edge not in a[0]:
                a[1] += [edge]

        if len(a[1]) < low_count:
            low_count = len(a[1])

    return low_count


glo_low = 500
"""
for i in range(1, 201):
    trial_low = len(graph[i])
    if trial_low < glo_low:
        glo_low = trial_low
    print(glo_low)

"""
for i in range(1, 201):
    trial_low = approx_min_cut_find(graph, nodes, i)
    if trial_low < glo_low:
        glo_low = trial_low

    print(glo_low)

