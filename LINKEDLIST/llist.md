# Linked Lists
Linked lists are a bit different from the Queue structure we just learned
about. Rather than owning a block of memory in a single location, each
element of the list has its own piece of memory which does not need to be
next to another part of the list. To understand this better we will start
by looking at the structure of a linked list to see how it is organized.
## Anatomy of a Linked List
Every linked list knows where it starts and where ends. This is important
since if we do not have this information the list can not be accessed.
Consider the following diagram:

![List Structure](catanatomy.jpg)
[1](#Sources)

We call the beginning of the list the 'head' and the end of the list the
'tail'. In between each of these resides the bulk of the linked list, organized into
what we call nodes. Each of these nodes located between the head and the 
tail store both the value and the address of the next node. Note that both
the head and their tail are their own individual node. When the address stored in
the Node becomes none we have found the tail.

A node can be visualized as the following:

![Node](nodecat.jpg)
[2](#Sources)

# Variations
## Doubly Linked Lists
![Doubly Linked Cat](dllist.jpg)
[3](#Sources)

There are two main types of linked lists, the first being singly-linked lists,
which we have been discussing up to this point. The second is known as a doubly-linked
list (DLL). The key difference between them is that the DLL also stores a second
address of the previous node. This implementation allows for two way traversal
of the list. This also carries various performance benefits
which we will look at shortly.

If we draw out both types of list they would look like the following:

* Singly-Linked List - Notice how the final node on the tail has it's address
set to None to allow you to know when the end has been reached.
![SLL](lvisual.jpg)

* Doubly-Linked List - Notice how the tail is now able to access the prior
node, allowing for reverse traversal.
![DLL](dllvisual.jpg)

* Circular - These types of linked lists have a slight variation, the tail node
stores the address of the head node to be quickly able to go around the list.
We will not cover this type of list in depth here but it is good to be aware
it exists.

# Linked List Complexity
Here is a table comparing SLL to DLL complexitys. When in python we can use the
deque class to implement a DLL, and an example of the operation is provided.

|    Operation:   | SLL: | DLL: |   Python Example: (DLL only)  |                                 Rationale:                                |
|:---------------:|:----:|:----:|:-----------------------------:|:-------------------------------------------------------------------------:|
|   Insert Head   | O(1) | O(1) |     deque.appendleft(data)    |                Only the head node needs changed to insert.                |
| Insert at Index | O(n) | O(n) |  deque.insert(position, data) |                    Must loop until the index is found.                    |
|   Insert Tail   | O(n) | O(1) |       deque.append(data)      | A SLL must loop to the end, but a DLL can adjust the tail address easily. |
|   Remove Head   | O(1) | O(1) |        deque.popleft()        |                Only the head node needs changed to remove.                |
| Remove at Index | O(n) | O(n) |      deque.remove(index)      |                    Must loop until the index is found.                    |
|   Remove Tail   | O(n) | O(1) |          deque.pop()          |     A SLL must loop to the end, but a DLL can adjust the tail address.    |
|     Size of     | O(1) | O(1) |           len(deque)          |                        Size is stored by the class.                       |
|     Is Empty    | O(1) | O(1) |        len(deque) == 0        |                     Easy to check the size against 0.                     |
|     Index of    | O(n) | O(n) | deque.index(item, begin, end) |               Must loop through the list in order to search.              |

Notice how the performance changes depending on the type of list. By gaining access
to the tail via a DLL we can greatly reduce the number of steps required for
various operations.

# Linked List Operations
Since there are no traditional indexes when using a linked list, we need to know
where we are. We typically store this as a variable named 'current'. To enter the
list we need to set current to either be located at the head or tail. From there
we can walk through the list by assigning current to the references in the nodes
with current <- current.next or current <- current.previous. This will set us on track
to access the next nodes.

![Linked List Cat](listcat.png)
[4](#Sources)

As a general rule we should always know where the head and tail are in a DLL
Losing access to this would lose access to the list. This can be tricky so we will
cover a few of the operations.
Performing the operations:
* Insert Head - Once you have a node to be inserted, the next of your newnode
should be addressed to the head. ```newnode.next = DLL.head``` and the previous of the head
should be assigned to the node. ```DLL.head.prev = newnode``` 
* Insert in Middle - Once you have a node to be inserted, these steps will
ensure you maintain the integrity of the list. The red arrows mark a reference that
has been reassigned.

# Exercises
1. Create a program to convert the following premade deque into a python list,
storing all the values from the deque into the array. The items must remain in the same
 order. A solution to this problem can be found at the bottom of the page.
```python
from collections import deque

def fill_deque(my_deque):
    for i in range(10):
        my_deque.append("cat" + str(i))

def deque_to_array(my_deque, cat_list):
    # Your code here. Try to find the best solution.

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
```

#Solutions
1. There are a few ways to solve this problem. 
```python
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

```

#### Sources:
1. Mr. Scruffles
1. <a name = "image3"></a>https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F838091811897583826%2F&psig=AOvVaw3SpZF-kfkwELuiYGLWW_24&ust=1607204720956000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOD0va2mte0CFQAAAAAdAAAAABAL
1. <a name = "image1"></a>https://www.reddit.com/r/ProgrammerHumor/comments/fbbdl3/linked_cat/
2. <a name = "image2"></a>https://www.catster.com/wp-content/uploads/2019/05/Two-orange-ginger-tabbies-wrestling-fighting-and-biting.jpg