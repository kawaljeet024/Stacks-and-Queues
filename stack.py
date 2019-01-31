class stack():
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items


s = stack()
s.push("100")
s.push("200")
print(s.get_stack())
s.push("300")
print(s.get_stack())
s.pop()
print(s.get_stack())
