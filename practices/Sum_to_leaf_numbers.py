class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
rootArray = [1,2,3]
root = Node(rootArray[0])
print('root',root.data)
for i in range(1,len(rootArray)-1):
    root.insert(rootArray[i])

root.PrintTree()
print('root',root.data)

def sumNumbers( root ) :
    rtl = []
    def dfs(root):
        if root: 
            print(root.data)
            dfs(root.left)
            dfs(root.right)
        return False

sumNumbers(root)