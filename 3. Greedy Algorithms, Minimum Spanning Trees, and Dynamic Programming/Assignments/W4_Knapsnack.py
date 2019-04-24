"""
Week 4 Assignment Questions
"""


"""
###################################################################################################
# Question 1
import pandas

file = open("W4_Data_Q1.txt", 'r')
data = file.readlines()
data.pop(0)  # Removing summary info header
itemw = [(0, 0)]
for line in data:
    elements = line.split()
    itemw += [(int(elements[0]), int(elements[1]))]


# getting the 2d array ready
col = [i for i in range(10001)]
rows = [i for i in range(101)]
df = pandas.DataFrame(columns=col, index=rows)
df.fillna(value=0, inplace=True)

#the dp algorithm
for row in range(1, 101):
    for col in range(1, 10001):
        value = itemw[row][0]
        weight = itemw[row][1]

        if col - weight < 0:
            df.iloc[row][col] = df.iloc[row - 1][col]
        else:
            df.iloc[row][col] = max(df.iloc[row - 1][col], df.iloc[row - 1][col - weight] + value)


print(df.iloc[100][10000])

#ans is 2493893
"""
    
###################################################################################################
# Question 2


BC = 2000000


class KeyPoint:
    def __init__(self, value, position):
        self.value = value
        self.position = position

    def val(self):
        return self.value

    def pos(self):
        return self.position

    def vp(self):
        return str(self.value) + " " + str(self.position)


file = open("W4_Data_Q2.txt", 'r')
data = file.readlines()
data.pop(0)  # Removing summary info header
itemw = []
for line in data:
    elements = line.split()
    itemw += [KeyPoint(int(elements[0]), int(elements[1]))]


itemw.sort(key=lambda x: x.pos(), reverse=True)


print("hey1")

current = [KeyPoint(0, 0)]
new = [KeyPoint(0, 0)]
counter = 0
for item in itemw:
    for kp in current:
        if kp.pos() + item.pos() <= BC:
            new += [KeyPoint(kp.val() + item.val(), kp.pos() + item.pos())]
        else:
            break

    new.sort(key=lambda x: x.pos())

    nc = 0
    while nc < len(new) - 2:
        if new[nc].val() >= new[nc + 1].val():
            new.pop(nc + 1)
        else:
            nc += 1

    current = new[:]
    counter += 1

current.sort(key=lambda x: x.val())
print(current[-1].val())
print(current[-1].pos())


#answer is 4243395





