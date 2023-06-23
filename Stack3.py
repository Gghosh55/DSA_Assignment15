class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, element):
        self.q1.append(element)

    def pop(self):
        if not self.q1:
            return "Stack is empty"

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        popped_element = self.q1.pop(0)

        self.q1, self.q2 = self.q2, self.q1

        return popped_element

    def top(self):
        if not self.q1:
            return "Stack is empty"

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        top_element = self.q1[0]

        self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

        return top_element

    def isEmpty(self):
        return len(self.q1) == 0 and len(self.q2) == 0
stack = Stack()

stack.push(2)
stack.push(3)
stack.pop()
stack.push(4)
stack.pop()

print(stack.pop())


print(stack.isEmpty())
