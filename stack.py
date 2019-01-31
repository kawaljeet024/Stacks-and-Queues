class stack():
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def get_stack(self):
        return self.items


s = stack()
# print(s.isEmpty())
s.push("100")
s.push("200")
s.push("300")
s.push("400")
print(s.isEmpty())
print(s.get_stack())
print(s.peek())
