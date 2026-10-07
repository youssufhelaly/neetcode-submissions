class MyQueue:

    def __init__(self):
        self.index = 0
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        val = self.stack[0]
        self.stack = self.stack[1:]
        return val
        if self.stack:
            print(self.stack)
            val = self.stack[self.index]
            self.stack = self.stack[1:]
            self.index += 1
            if len(self.stack) == 0:
                self.index = 0
            else:
                self.index = self.index % len(self.stack) 
            return self.stack[0]
        else:
            return

    def peek(self) -> int:
        return self.stack[self.index]

    def empty(self) -> bool:
        return self.stack == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()