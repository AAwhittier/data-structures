class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self._insert(value, self.root)

    def _insert(self, value, node=None):
        if self.root is None:
            self.root = Node(value)
        else:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    self._insert(value, node.left)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    self._insert(value, node.right)

    def display(self):
        self._display(self.root)

    def _display(self, node):
        if node is not None:
            print(node.value)
            self._display(node.left)
            self._display(node.right)

    def height_of_branches(self):
        if self.root is None:
            return 0
        else:
            return self._height_of_left(self.root), self._height_of_right(self.root)

    def _height_of_left(self, node):
        if node is None:
            return 0
        else:
            return self._height_of_left(node.left) + 1

    def _height_of_right(self, node):
        if node is None:
            return 0
        else:
            return self._height_of_right(node.right) + 1

christmas_tree = Tree()
christmas_tree.insert(5)
christmas_tree.insert(4)
christmas_tree.insert(6)
christmas_tree.insert(3)
christmas_tree.insert(7)

height = christmas_tree.height_of_branches()
if height[0] == height[1]:
    print("Your cat can safely climb the tree.")
else:
    print("You cat would cause the tree to fall over.")
