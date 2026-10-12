class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            tmp = self.minStack.pop()
            self.minStack.append(tmp)
            self.minStack.append(min(tmp,val))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if not self.stack:
            return
        tmp = self.stack.pop()
        self.stack.append(tmp)
        return tmp

    def getMin(self) -> int:
        if not self.minStack:
            return
        tmp = self.minStack.pop()
        self.minStack.append(tmp)
        return tmp
