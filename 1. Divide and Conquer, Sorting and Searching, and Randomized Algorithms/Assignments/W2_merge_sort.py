"""
Code for the week 2 assignment
"""

import math

txt_file = open("W2_integer_array.txt", 'r')
text_numbers = txt_file.readlines()
numbers = []
for i in text_numbers:
    numbers += [int(i)]


def merge_sort(lst):
    """
    :param lst: a list of elements
    :return: a sorted list of element in ascending order
    """

    mid = int(math.floor(len(lst) / 2))
    a = lst[:mid]
    b = lst[mid:]

    if mid == 0:
        return lst

    else:
        # merge step below:
        sorted_lst = []
        sorted_a = merge_sort(a)
        sorted_b = merge_sort(b)

        while len(sorted_a) * len(sorted_b) > 0:
            if sorted_a[0] < sorted_b[0]:
                next_item = sorted_a.pop(0)
            else:
                next_item = sorted_b.pop(0)

            sorted_lst += [next_item]

        #Append elements remaining in sorted_a or sorted_b
        sorted_lst += sorted_a
        sorted_lst += sorted_b

    return sorted_lst


def count_inversions(lst):
    """
    :param lst: a list of elements
    :return: a list containing:
                an integer representing the number of inversions
                a list that contains the elements of lst in ascending order
    """

    mid = int(math.floor(len(lst) / 2))
    a = lst[:mid]
    b = lst[mid:]

    if mid == 0:
        return [0, lst]

    else:
        # merge step below:
        inv_a = count_inversions(a)
        inv_b = count_inversions(b)

        num_inv = inv_a[0] + inv_b[0]

        sorted_lst = []
        sorted_a = inv_a[1]
        sorted_b = inv_b[1]

        while len(sorted_a) * len(sorted_b) > 0:
            if sorted_a[0] < sorted_b[0]:
                next_item = sorted_a.pop(0)
            else:
                next_item = sorted_b.pop(0)
                num_inv += len(sorted_a)

            sorted_lst += [next_item]

        #Append elements remaining in sorted_a or sorted_b
        sorted_lst += sorted_a
        sorted_lst += sorted_b

    return [num_inv, sorted_lst]

print(count_inversions(numbers))

#answer is 2407905288

