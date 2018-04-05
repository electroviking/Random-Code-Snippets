class Node:
    # Contructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_triverse(root):
    pass


def pre_order_triverse(root):
    pass


def post_order_triverse(root):
    pass


# [40 , 30 , 35 , 80 , 100]

n = Node(40)
n.left = Node(30)
n.right = Node(80)
n.left.right = Node(100)
