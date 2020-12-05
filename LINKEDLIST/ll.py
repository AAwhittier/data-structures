from collections import deque

def fill_deque(my_deque):
    for i in range(10):
        my_deque.append("cat" + str(i))

def deque_to_array(my_deque, cat_list):
    while(len(my_deque) != 0):
        cat_list.append(my_deque.popleft())

def main():
    my_deque = deque()
    cat_list = []

    fill_deque(my_deque)
    print(my_deque)

    deque_to_array(my_deque, cat_list)
    print(cat_list)

    pass

if __name__ == '__main__':
    main()
