class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        # print(self.stack)

    def pop(self):
        """
        :rtype: void
        """
        a = self.stack[-1]
        # print(a)
        self.stack = self.stack[:-1]
        # print(self.stack)

    def top(self):
        """
        :rtype: int
        """
        a = self.stack[-1]
        return a

    def getMin(self):
        """
        :rtype: int
        """
        a = self.stack[0]
        for i in self.stack:
            if i < a:
                a = i
        return a


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()