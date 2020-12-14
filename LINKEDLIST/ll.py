from collections import deque

def fill_list():
    cat_list = []
    for i in range(10):
        cat_list.append("cat" + str(i))
    return cat_list

def convert_list_to_deque(my_list):
    my_deque = deque()
    for item in my_list:
        my_deque.append(item)
    return my_deque

cat_list = fill_list()
my_deque = deque()
my_deque = convert_list_to_deque(cat_list)
print(my_deque)

my_deque.reverse()
print(my_deque)