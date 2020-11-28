#Data Structures Tutorial
Welcome to my data structures tutorial. This tutorial will start by
covering Big-O notation, a key skill to be able to apply the topics
we will learn about here. We will then learn about both Queues and Linked
Lists. From there we will cover recursion in order to be able to learn about
our final topic, Trees.

**Start here:**
1. [Big O Notation](BIGO/big-o.md)
2. [Queues](QUEUE/queue.md)

\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\




# data-structures
DS Tutorial
# Data Structures Tutorial
## Big O Performance
1. What is it
    1. Why it matters
2. How to calculate
    1. Types of performance
    1. Graph of performance
3. Python performance example
    
# 
## Queue
#### Purpose of a Queue
#### Queue Structure
1. Types of Queues
1. FIFO
    * Back
    * Front
1. EX: Printer use of a queue
#### Queue Operations and complexity
1. Enqueue O(1)
1. Dequeue O(1)
1. Peek O(1)
1. isEmpty O(1)
1. isFull O(1)
#### Python Queues
1. Using a list as a queue
    * Example
    * Operations
#### Queue Examples
1. EX1: Fill queue
2. EX2: Pop queue 
1. Problem 1: Reverse a Queue
    * Solution
2. Problem 2 
#
## Linked List
#### Purpose of Linked List
#####What is a Linked List?
1. Types of Linked Lists Single-Double-Circular
1. Node
1. Data
1. Head
1. Tail
#####Linked List Operations and Complexity
1. Lookup O(n)
    * By index O(n)
2. Insert
    * At end O(1)
    * At beginning O(1)
    * In middle O(n)
3. Delete
    * At end O(n) DLL O(1)
    * At beginning O(1)
    * In middle O(1)
#### Usage Scenarios
1. When/why to use
    * Easy to resize
    * Use more memory
    * Want to insert in middle often
2. Real world example
##### Python examples and problem sets
1. EX1: Insert into middle
2. EX2: Delete head
1. Problem 1: Find middle of LL
    * Solution
2. Problem 2 Insert tail

## Recursion
1. Solve complex problem as smaller problems
1. Rules
    1. Base Case
    1. Smaller problem
1. Examples
    * Factorials
#### Tree
##### What is a tree
1. Hierarchy
    * Nodes
    * root - Parent - child - leaf
    * height
1. Tree types
    * Binary Trees
        * Balanced
        * left ^ node ^ right
    * AVL Trees
1. Example: Databases
    * Find a value
##### Tree Operations and Complexity 
1. Lookup O(log n)
1. Insert O(log n)
1. Delete O(log n)
#### Trees in python
1. Node structure value-left-right
1. Root
#### Examples
1. Find height from root
    * Solution
1. Find maximum value in a tree
