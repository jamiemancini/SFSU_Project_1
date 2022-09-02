import random


#arguments are the number of elements in the list (1000)
#AND the value of the elements in the list (values betw 100  and 10000)

def create_list(num_elements, start_value, end_value):
    """makes a list of elements with values between specified values"""

    list = []

    for i in range(num_elements):
        list.append(random.randrange(start_value, end_value,1))

    return list

#Caluclate the mean of the list

def find_mean(list):
    length = len(list)
    total = 0
    for item in list:
        total = total + item
    mean = total / length
    return mean

