class Node:
    # Contructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


hmap = {}


# Iterative Method to print the height of binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    level = 0

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        print "level", level
        print "queu len ", len(queue)
        if len(queue) > 1:
            if level >= 2:
                print queue[1].data
                # print queue[2].data
            else:
                print queue[0].data
                print queue[1].data
        else:
            print queue[0].data

        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver program
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(9)
root.right.right = Node(20)
printLevelOrder(root)
