n = int(input())

class stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) == 0:
            value = Node(value)
            self.stack.append(value)
        elif value > self.stack[-1] .value:
            value = Node(value)
            self.stack.append(value)
        else:
            self.stack[-1].after += 1

    def pop(self):
        if self.stack[-1].after == 0:
            self.stack.pop()
        else:
            self.stack[-1].after -= 1

    def max_val(self):
        return self.stack[-1].value

class Node(object):
    def __init__(self, value):
        self.value = value
        self.after = 0

s = stack()
for _ in range(n):
    var = input()
    if 'max' in var:
        print(s.max_val())
    if 'pop' in var:
        s.pop()
    if 'push' in var:
        s.push(int(var[5:]))

