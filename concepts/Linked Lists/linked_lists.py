

# First  of all create a node

class Node:
    def __init__(self, data = None):
        self.data = data
        self.nextval = None

# Define the linked list which is combination of nodes
class SLinkedList():
    def __init__(self):
      self.headval = None

# create and instance of the single linked list class
list1 = SLinkedList()

# add values to the linked list list1

list1.headval = Node("Mon")

node2 = Node("Tue")
node3 = Node("Wed")

# Link the nodes to each other

list1.headval.nextval = node2
node2.nextval = node3