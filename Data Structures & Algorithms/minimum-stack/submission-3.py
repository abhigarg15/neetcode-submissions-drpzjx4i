class MinStack:

    def __init__(self):
        self.st = []
        self.minVal = []

    def push(self, val: int) -> None:
        if self.minVal:
            self.minVal.append(min(self.minVal[-1],val))
            self.st.append(val)
        else:
            self.minVal.append(val)
            self.st.append(val)

    def pop(self) -> None:
        if self.st:
            self.st.pop()
            self.minVal.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
