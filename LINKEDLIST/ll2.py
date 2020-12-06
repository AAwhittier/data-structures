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

    def replace(self, target, value):
        current = self.head
        while current is not None:
            if current.data == target:
                current.data = value
            current = current.next

ll = LinkedList()
missing_cats = "Everybody wants to be a dog - Because a dog is the only dog - Who knows where it's at."
for word in missing_cats.split(" "):
    ll.append(word)

ll.replace("dog", "cat")
print(ll)
# Correct Outputs:
# Everybody wants to be a cat - Because a cat is the only cat - Who knows where it's at.