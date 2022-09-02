import random

#make your list of random numbers:

list = []

for i in range(10, 1000):
        list.append(random.randrange(100, 1000,1))

#Caluclate the mean of the list

def find_mean(list):
    length = len(list)
    total = 0
    for item in list:
        total = total + item
    mean = total / length
    return mean

