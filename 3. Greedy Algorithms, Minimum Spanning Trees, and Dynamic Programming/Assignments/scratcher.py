###################################################################################################
# Question 2


BC = 2000000


class KeyPoint:
    def __init__(self, value, position, ):
        self.value = value
        self.position = position

    def val(self):
        return self.value

    def pos(self):
        return self.position

    def dense(self):
        return int(self.value/self.position)

    def vp(self):
        return str(self.value) + " " + str(self.position)


file = open("W4_Data_Q2.txt", 'r')
data = file.readlines()
data.pop(0)  # Removing summary info header
itemw = []
for line in data:
    elements = line.split()
    itemw += [KeyPoint(int(elements[0]), int(elements[1]))]


print(itemw[1].dense())

itemw.sort(key=lambda x: x.dense(), reverse=True)

print("hey1")

current = [KeyPoint(0, 0)]
new = [KeyPoint(0, 0)]
counter = 0
for item in itemw:
    for kp in current:
        if kp.pos() + item.pos() <= BC:
            new += [KeyPoint(kp.val() + item.val(), kp.pos() + item.pos())]

    new.sort(key=lambda x: x.pos())

    nc = 0
    while nc < len(new) - 2:
        if new[nc].val() >= new[nc + 1].val():
            new.pop(nc + 1)

        nc += 1

    current = new[:]
    counter += 1
    print(counter)
    print(len(new))
    print(new[-1].pos())
    print()


print("hey2")
current.sort(key=lambda x: x.val())
print(current[-1].val())
