# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import datetime
import random

random_number_zero_to_1 = random.random()
print(str(random_number_zero_to_1))
random_number_1_to_10 = random.randint(1, 10)
print(str(random_number_1_to_10))

# 2) Use the datetime library together with the random number to generate a random, unique value.

unique_value = str(datetime.datetime.now()) + str(random_number_1_to_10)

print(unique_value)
