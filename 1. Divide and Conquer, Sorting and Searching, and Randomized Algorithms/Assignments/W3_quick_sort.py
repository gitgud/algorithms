"""
Quick Sort
"""


import copy
import math

txt_file = open("W3_integer_array.txt", 'r')
text_numbers = txt_file.readlines()
numbers = []
for i in text_numbers:
    numbers += [int(i)]

num_comparisons = 0


def quick_sort(lst, recursive_function):
    """
    :param lst: a list of integers
    :param recursive_function: a function that quicksort recursively calls to sort the left and right sides of the pivot
    :return: a sorted list using quick sort and the first element as the pivot
    """

    global num_comparisons
    length = len(lst)

    #if the base case of length < 2 is present skip to the return statement at the end

    if length > 1:
        pivot = lst[0]
        i = 1
        num_comparisons += length - 1

        for j in range(1, length):
            if lst[j] < pivot:
                ith_entry = lst[i]
                lst[i] = lst[j]
                lst[j] = ith_entry
                i += 1

        # swapping pivot into correct position
        lst[0] = lst[i - 1]
        lst[i-1] = pivot

        #running qs on left and right sides of pivot
        left = recursive_function(lst[0:i - 1])
        right = recursive_function(lst[i:])

        lst = left + [pivot] + right

    return lst


def q1_quick_sort(lst):
    """
    :param lst: a list of integers
    :return: a sorted list using quick sort and the first element as the pivot
    """

    return quick_sort(lst, q1_quick_sort)


def q2_quick_sort(lst):
    """
    :param lst: a list of integers
    :return: a sorted list using quick sort and the last element as the pivot
    """

    if len(lst) > 1:
        pivot = lst[-1]
        lst[-1] = lst[0]
        lst[0] = pivot

    return quick_sort(lst, q2_quick_sort)


def q3_quick_sort(lst):
    """
    :param lst: a list of integers
    :return: a sorted list via quick sort and pivot = the median of [lst[0], lst[floor(len(lst)/2)] and lst[-1]]
    """

    if len(lst) > 2:
        first_mid_last = [lst[0], lst[math.ceil(len(lst)/2) - 1], lst[-1]]

        pivot = sum(first_mid_last) - max(first_mid_last) - min(first_mid_last)
        pivot_index = lst.index(pivot)

        lst[pivot_index] = lst[0]
        lst[0] = pivot

    return quick_sort(lst, q3_quick_sort)

"""

################################################################################################
#Q1
print('Q1')
num_comparisons = 0
print(q1_quick_sort(copy.deepcopy(numbers)))
print(num_comparisons)
print()
#ANSWER: 162085 comparisons


################################################################################################
#Q2
print('Q2')
num_comparisons = 0
print(q2_quick_sort(copy.deepcopy(numbers)))
print(num_comparisons)
print()
#ANSWER: 164123 comparisons


################################################################################################
#Q3
print('Q3')
num_comparisons = 0
print(q3_quick_sort(copy.deepcopy(numbers)))
print(num_comparisons)
print()
#ANSWER: 138382 comparisons

"""