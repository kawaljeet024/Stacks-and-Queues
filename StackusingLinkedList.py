class StackNode():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode

    def pop(self):
        if(self.isEmpty()):
            return "-1"
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped


stack = Stack()
stack.push("11")
stack.push("12")
stack.push("13")
print(stack.pop())
