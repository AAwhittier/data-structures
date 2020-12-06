from collections import deque

def fill_deque(my_deque):
    for i in range(10):
        my_deque.append("cat" + str(i))

def deque_to_ll(my_deque, cat_list, linked_list):
    # Your code here.
    pass

my_deque = deque()
cat_list = fill_deque(my_deque)
