"""
The 2 sum problem
"""


##############################################################
#Import data and get rid of duplicates

numbers = set([])
file = open('W4_data.txt', 'r')
data = file.readlines()
for num in data:
    numbers.add(int(num))
file.close()
print("Data imported, there are:", len(numbers), "unique integers")

#Sorting the numbers
num_copy  = []
for num in numbers:
    num_copy += [int(num)]
num_copy.sort()
numbers = num_copy
del num_copy


##############################################################
#Write the sorted data to a file

file = open("W4_Data_Sorted.txt", 'w')
for num in numbers:
    file.write(str(num) + '\n')
file.close()


##############################################################
#Find unique sums between -10,000 and 10,000 inclusive

#looking at the set of numbers since all negative ints are < -10000 and all positive ints > 10000, acceptable sums can
#only exist when a negative and positive integer are combined.


numbers = numbers #sorted list
neg_nums = numbers[:499875]
pos_nums = numbers[499875:]
sums = set([])
current_pos = 0
last_start = len(pos_nums) - 1

#getting rid of all the numbers that are too negative
while neg_nums[0] + numbers[-1] < -10000:
    neg_nums.pop(0)



while len(neg_nums)*len(pos_nums) > 0:
    num = neg_nums.pop(0)
    counter = None #will be set later

    #getting rid of any numbers that are too big
    while len(pos_nums) > 0 and num + pos_nums[-1] > 10000:
        pos_nums.pop()
        if len(pos_nums) == 0:
            print("len(pos_nums) == 0, sums:",  len(sums))
            #crash happens here, but i don't care.

    counter = len(pos_nums) - 1
    while len(pos_nums) > 0 and counter > -1 and num + pos_nums[counter] >= -10000:
        sum = num + pos_nums[counter]
        if sum not in sums:
            sums.add(sum)
        counter -= 1


#print(len(sums))