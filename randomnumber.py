import random


def random_list(length):
    low_value = 0
    return random.sample(range(low_value, length), length)


"""
trial_array_length = 10000000
trial_array = random_list(trial_array_length)
"""

array_length1 = 300000
array1 = random_list(array_length1)

array_length2 = 500000
array2 = random_list(array_length2)

array_length3 = 1000000
array3 = random_list(array_length3)

array_length4 = 10000000
array4 = random_list(array_length4)

