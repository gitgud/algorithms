"""
W3 Assignment
"""

import sys
sys.setrecursionlimit(1000000)

### Importing Data
file = open('W3_Data_Q1.txt', 'r')
data = file.readlines()
data.pop(0)  # getting rid of the first line that shows how big the alphabet is


###  Defining Global Variables
cw = dict()
for i in range(len(data)):
    cw[str(i)] = int(data[i])
paths = dict()
counter = 0
codes = dict()  # dict, the original alphabet encoded. Key = char in alphabet, value = Huffman encoding


def huffman_graph():
    """
    return: str
    """

    global cw, paths, counter

    if len(cw) == 1:
        for final_keyasd in cw:
            print("asdasdkjasdkjn")
            return final_keyasd

    else:  # merging
        mink1 = min(cw, key=cw.get)
        minv1 = cw[mink1]
        del cw[mink1]
        mink2 = min(cw, key=cw.get)
        minv2 = cw[mink2]
        del cw[mink2]

        paths["T" + str(counter)] = [['0', mink1], ['1', mink2]]
        cw["T" + str(counter)] = minv1 + minv2
        counter += 1

        huffman_graph()


def huffman_codes(starting, a_code):
    """
    :param starting: node to start traversal on
    :param a_code: short for accumulated code, str made up of '0's and '1's
    :return: None. updates the global variable codes
    """

    global paths, codes

    for edge_info in paths[starting]:
        if edge_info[1][0] != 'T':
            codes[edge_info[1]] = a_code + edge_info[0]
        else:
            huffman_codes(edge_info[1], a_code + edge_info[0])

"""
start123 = huffman_graph()
print(start123)
huffman_codes("T998", "")

###  The min and max length huffman codes:
min_code = float('inf')
max_code = 0
for key in codes:
    if len(codes[key]) < min_code:
        min_code = len(codes[key])

    if len(codes[key]) > max_code:
        max_code = len(codes[key])

print(min_code)
print(max_code)
"""


##############################
# Question 3


file = open("W3_Data_Q3.txt", "r")
data = file.readlines()
data.pop(0)  # Removing the number of nodes in the path graph
nw = dict()
for i in range(len(data)):
    nw[i + 1] = int(data[i])

# Data Structures
a = [0, nw[1]]  # Accumulative table of max weights. Element in ith position of i reps the max weight up until ith node

def mw():
    """
    mw stands for max weight
    :return: None, updates global variable a by appending elements up until a represents all the nodes in nw
    """
    global a, nw

    for i in range(2, len(nw) + 1):
        a += [max(a[i-1], a[i-2] + nw[i])]


def mw_nodes():
    """
    :return: a list of all nodes in the max weight (mw) set
    """

    global a, nw

    counter = 3
    group1 = [1]
    group2 = [2]

    while counter < len(a):

        #finding out what node to add:
        if a[counter] == a[counter - 2] + nw[counter]:
            if counter % 2 == 1:
                group1 += [counter]
            else:
                group1 += [counter]

        else:
            if counter % 2 == 1:
                group1 = list(group2)
            else:
                group2 = list(group1)

        counter += 1


    if len(a) %2 == 0:
        return group1
    else:
        return group2

mw()
max_weight_nodes = mw_nodes()

#1, 2, 3, 4, 17, 117, 517, and 997
print("1 in max_weight_nodes", 1 in max_weight_nodes)
print("2 in max_weight_nodes", 2 in max_weight_nodes)
print("3 in max_weight_nodes", 3 in max_weight_nodes)
print("4 in max_weight_nodes", 4 in max_weight_nodes)
print("17 in max_weight_nodes", 17 in max_weight_nodes)
print("117 in max_weight_nodes", 117 in max_weight_nodes)
print("517 in max_weight_nodes", 517 in max_weight_nodes)
print("997 in max_weight_nodes", 997 in max_weight_nodes)

#answer is 10100110