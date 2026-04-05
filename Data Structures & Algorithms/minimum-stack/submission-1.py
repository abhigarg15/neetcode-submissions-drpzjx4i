class MinStack:

    def __init__(self):
        self.arr = []        
        self.minVal = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minVal) == 0:
            self.minVal.append(val)
        else:
            val = min(val, self.minVal[-1])
            self.minVal.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.minVal.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
