class TwoStackArr:
    def __init__(self, n):
        self.n = n
        self.stack = [None] * self.n
        self.top1 = -1
        self.top2 = n
    
    def push1(self, n):
        if(self.top1 < self.top2 - 1):
            self.top1 += 1
            self.stack[self.top1] = n
            print(self.stack)
        else:
            print("stack1 overflow")
    
    def pop1(self):
        if(self.top1 >= 0):
            self.stack[self.top1] = None
            self.top1 -= 1
            print(self.stack)
        else:
            print("stack1 underflow")
    
    def push2(self, n):
        if(self.top2 > self.top1 + 1):
            self.top2 -= 1
            self.stack[self.top2] = n
            print(self.stack)
        else:
            print("stack2 overflow")
    
    def pop2(self):
        if(self.top2 <= self.n - 1):
            self.stack[self.top2] = None
            self.top2 += 1
            print(self.stack)
        else:
            print("stack2 underflow")

ts = TwoStackArr(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
ts.push2(40)
ts.pop1()
ts.pop1()
ts.pop1()