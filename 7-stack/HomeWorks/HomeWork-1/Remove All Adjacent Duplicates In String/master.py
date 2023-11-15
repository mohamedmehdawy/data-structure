class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        # check if the string is less than 1, if true return the string
        if len(s) < 2:
            return s
        
        # create stack
        stack = []
        
        for char in s:
            # check if the stack is empty append the char or the last element not = the current char
            if not stack or char != stack[-1]:
                stack.append(char)
            else:
                stack.pop()
        
        # return the string
        return "".join(stack)