# Using two stacks: stack and minstack
# minstack을 추가적으로 만들어서 현재 minimum value를 저장하면
# O(1) time complexity로 getMin() 함수를 구현할 수 있다.
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.min = None

    def push(self, val):
        self.stack.append(val)
        minval = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(minval)

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]
