
#! randomization in python is a method where computer generated random numbers in a given range. to use this function we need to import a module in python by using "import random" at the start of the program. we use randint() to generate random number between 2 points and can generate that points too eg random.randint(1,10) means it can generate 1<= x <= 10 . another is random.random() which generates from 0 to 1. another is uniform() which generates random float within the given range

import random
# # random_integer = random.randint(1,10)
# #
# #
# # print(random_integer)
#
# # random_number_0_to_1 = random.random()
# # print(random_number_0_to_1)
#
# random_float = random.uniform(1,10)
# print(random_float)

choice = random.randint(0,1)
if choice == 0:
    print ("Heads")
else :
    print ("Tails")