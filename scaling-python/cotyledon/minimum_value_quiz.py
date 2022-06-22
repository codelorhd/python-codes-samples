"""You are given a list of one million integers named mylist. If you are asked to compute the minimum of the list.
"""


# Relevant libraries are imported already
from concurrent.futures import thread
import random
import threading

# mylist contains 1 million entries ranging from 1 to 100000000
mylist = [random.randint(1, 100000000) for i in range(1000000)]
minimum = 0
minimums = []

########
# Your code goes here #


def calc_min(li):
    _minimum = li[0]
    for x in li:
        if x < _minimum:
            _minimum = x
    minimums.append(_minimum)


# This can be divided further!
first_chunk = mylist[0 : (len(mylist) // 2)]
second_chunk = mylist[(len(mylist) // 2) + 1 : len(mylist)]


first_thread = threading.Thread(
    target=calc_min,
    args=(first_chunk,),
)
second_thread = threading.Thread(target=calc_min, args=(second_chunk,))

first_thread.daemon = True
second_thread.daemon = True
first_thread.run()
second_thread.run()
minimum = min(minimums)

#   Code until here   #
########

# Result:
print(
    "Global Minimum: ",
    minimum,
)
