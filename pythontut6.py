import random, math
# Generate randon values between 1 and 9 to populate a list

randList = []

for i in range(9):
    randList.append(random.randrange(1, 9))
print(randList)