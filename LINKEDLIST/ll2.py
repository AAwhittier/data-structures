class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        output = []
        current = self.head
        while current is not None:
            output.append(current.data)
            current = current.next
        return " ".join(output)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def find(self, value):
        # Place your code here.
        pass


ll = LinkedList()
lostcat = "Everybody wants to be a cat. Because a cat's the only cat. Who knows where it's at."
for word in lostcat.split(" "):
    ll.append(word)

# Find the cat here.
print(ll)