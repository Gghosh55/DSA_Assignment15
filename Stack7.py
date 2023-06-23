class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1][0]:
            self.min_stack.append((val, len(self.stack) - 1))

    def pop(self):
        if self.stack:
            popped_element = self.stack.pop()

            if popped_element == self.min_stack[-1][0]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1][0]

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())
min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())
