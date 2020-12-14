# Trees
Trees begin at a **root** and are composed of **nodes**. Each node stores
its own data and the addresses of its **children**. This creates
a hierarchy for each of the individual nodes. This structure can be
useful in areas such as database indexes, file compression, and autocompletion
algorithms. Unlike the Linked List nodes
we diagrammed earlier the structure of tree nodes look a bit more like the following:

![Tree Node](treenode.jpg)
[1](#Sources)

The **root** is the first Node of any tree, and the first Node of any subtree
is a **parent**, along with any node that has children. 
Each Node may have any amount of children. If a Node has no Children it is
referred to as a **leaf node**. Trees can also support reverse lookup by allowing
a child node to store the address of it's parent. If each parent node only
allows for two child nodes, the tree becomes known as a **binary tree**.

## Binary Search Trees
**Binary Search Trees** allow for quick lookup of the data they store. In a
BST the value of a node is always greater than the child on the left, and less
than the value of the child on the right. ```left child < parent < right child```
This rule applys to all subtrees. 

If we follow this rule and ensure that the maximum distance from the root, known as
the **height** of the tree is the same on either side, we can discard half of the 
tree when searching. This results in an O(n/2) operation or O(log n). Here is a
diagram of a balanced BST:

![Balanced Tree](balanced.JPG)

If we want to insert a value the operations we would need
to follow are the following:

![12 Inserted](insert12.JPG)

1. Starting at the root, compare the inserting value to the root value.
In this case, our value is lower so we go left.
1. Compare the value to the left child, if no child exists, insert it. Since 12 is
less than 20, we stay left.
2. Compare the value to the following nodes until you find an empty spot. In this case
our value is greater than 11, so we go right and insert at the open location.

We can insert 12 without changing the height. 
find - log n
insert o log n - Need to lookup where node belongs
delete 0 log n - Need to lookup the node to delete.


[Return to homepage](../README.md)

### Sources
1. http://cats.ava7.com/domestic-cat/mother-cat-with-two-of-her-6-week-kittens.html