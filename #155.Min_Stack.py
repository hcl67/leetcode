'''
https://leetcode.com/problems/min-stack/
'''
class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s += [val]
        if len(self.m) == 0:
            self.m += [val]
        else:
            self.m += [min(val,self.m[-1])]

    def pop(self) -> None:
        del self.s[-1]
        del self.m[-1]

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
