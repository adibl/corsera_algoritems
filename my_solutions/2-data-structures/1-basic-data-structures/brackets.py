# import pytest

class node(object):
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer


class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, value):
        last_head = self.head
        self.head = node(value, last_head)

    def pop(self):
        if self.head == None:
            return None
        ret = self.head.value
        self.head = self.head.pointer
        return ret

    def top(self):
        if self.head == None:
            return None
        else:
            return self.head.value

    def is_empty(self):
        return self.head == None

PAIRS = { '[': ']', '{': '}', '(': ')'}
def check_brackets(arr):
    stack = Stack()
    for i in range(len(arr)):
        string = arr[i]
        if string in PAIRS.keys():
            stack.push(string)
        elif string in PAIRS.values():
            if PAIRS.get(stack.top()) == string:
                stack.pop()
            else:
                return i + 1
    if stack.is_empty():
        return True
    else:
        return len(arr)


def main():
    arr = list(input())
    result = check_brackets(arr)
    if result is True:
        print('Success')
    else:
        print(result)



if __name__ == "__main__":
    main()

"""
def test_stack_all():
    s = Stack()
    s.push(3)
    s.push(5)
    assert s.pop() == 5
    assert s.is_empty() == False
    assert s.pop() == 3
    assert s.is_empty() == True

@pytest.mark.parametrize("inp,result", [
    pytest.param("[]{}()", True),
    pytest.param("[asdfl]{asdfasdf}(pfaef)", True),
    pytest.param("{({})}", True),
    pytest.param("[{}()",5),
    pytest.param("[{()]",5),
    pytest.param("[{})",4),
    pytest.param("))]]",1),
    pytest.param("(0{[()([a]",10),
    ],
    )
def test_brackets(inp, result):
    assert check_brackets(list(inp)) == result

"""
