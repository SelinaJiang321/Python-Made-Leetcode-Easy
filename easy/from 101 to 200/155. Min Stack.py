"""

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.

"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        # initialize a stack
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # .append() is a function that can add the element at the end of the stack
        self.stack.append(x)
        
        # we also want to add the minimum element to the end of minStack
        if not self.minStack or self.minStack[-1] >=x :
            self.minStack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        tmp = self.stack.pop()
        if tmp == self.minStack[-1] :
            # if it is the same element then we poped out the element of minStack
            self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        
        # return the top element
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # return the last element
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
