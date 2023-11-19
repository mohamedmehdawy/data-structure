class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        # if empty return 0
        if not s:
            return 0
        
        # create stack and scrore
        # stack will start with init state to store the scrore
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                # if is 0, this is not a parent
                value = max(2 * stack.pop(), 1)
                
                stack[-1] += value
                
        return stack[-1]