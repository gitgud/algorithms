"""
Median Maintenance
"""
import copy

#import the data
file = open("W3_Median.txt", 'r')
data = file.readlines()

numbers = []
for text_num in data:
    numbers += [int(text_num)]



heap = ["dummy"]


def insert(heap, node):
    """
    :param heap: list of int, representation of a heap
    :param node: int
    :return: None, modifies heap to include the new node
    """

    heap += [node]
    posNode = len(heap) - 1
    posSwap = parent(heap, posNode)

    while posSwap != posNode:
        swapNode = heap[posSwap]
        heap[posSwap] = heap[posNode]
        heap[posNode] = swapNode

        posNode = posSwap
        posSwap = parent(heap, posNode)

def parent(heap, posNode):
    """
    :param heap: list of int, representation of a heap
    :param posNode: int, the position in the heap where the node is
    :return: int, returns posNode if no swap is needed or the position in the heap to swap posNode with
    """
    answer = 0
    if posNode == 1:
        answer = posNode

    elif heap[posNode] >= heap[int(posNode/2)]:
        answer = posNode

    else:
        answer = int(posNode/2)

    return answer


def extractMin(heap):
    """
    :param heap: list of int, representation of a heap
    :return: Int: the min node in the heap. Also modifies heap to exclude the min node
    """

    minimum = heap[1]
    root = heap.pop()

    if len(heap) > 1:
        heap[1] = root
    else:
        heap += [root]


    posNode = 1

    while posNode * 2 <= len(heap) - 1:
        parentInfo = [heap[posNode], posNode]
        childA = [heap[posNode * 2], posNode * 2]
        childB = [float("inf"), -1]
        if len(heap) - 1 >= posNode * 2 + 1:
            childB = [heap[posNode * 2 + 1], posNode * 2 + 1]
        swapNode = min(parentInfo, childA, childB, key=lambda x:x[0])

        if parentInfo[0] == swapNode[0]:
            break

        #swapping
        heap[parentInfo[1]] = swapNode[0]
        heap[swapNode[1]] = parentInfo[0]
        posNode = swapNode[1]

    return minimum

"""
insert(heap, 1)
insert(heap, 2)
insert(heap, 6)
insert(heap, 8)
insert(heap, 10)
insert(heap, 3)
insert(heap, 4)
print(heap)
print()
extractMin(heap)
print(heap)
print()
extractMin(heap)
print(heap)
"""

"""
numbers = ['dummy', 1640, 6331, 2793, 9290]
insert(numbers, 225)
print(numbers)

"""

medians = []
length = 0

for number in numbers:
    length += 1
    insert(heap, number)
    heapCopy = copy.deepcopy(heap)

    numExtractions = (int(length/2))
    if length % 2 == 0:
        numExtractions -= 1

    if length % 2 == 1 and len(medians) > 0 and medians[-1] >= number:
        medians += [medians[-1]]

    elif length % 2 == 0 and len(medians) > 0 and medians[-1] <= number:
        medians += [medians[-1]]

    else:
        for i in range(numExtractions):
            extractMin(heapCopy)

        medians += [extractMin(heapCopy)]

    del heapCopy

print(sum(medians))
