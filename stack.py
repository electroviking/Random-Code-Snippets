class Stack():
    def __init__(self):
        self.stack = []

    def insert_item(self, data):
        self.stack.insert(0, data)

    def remove_item(self):
        self.stack.pop(0)

    def peek(self):
        if self.stack:
            return self.stack[0]
        return None


# [1,2,3]


def sort_stack():
    s = Stack()
    s.insert_item(1)
    s.insert_item(2)
    s.insert_item(3)
    print s.peek()


print sort_stack()
