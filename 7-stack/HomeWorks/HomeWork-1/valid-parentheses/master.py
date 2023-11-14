class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check if the length of the string is not have 2 pieces
        if len(s) % 2 != 0:
            return False
        
        # create the stack
        dct = {')': '(', '}':'{', ']':'['}
        stack = []
        
        for char in s:
            # if the current char is in open append it to the stack
            if char not in dct:
                stack.append(char)
            # if its the close, should be match with the open
            elif not stack or dct[char] != stack.pop():
                return False
        
        # if have elments in stack, this is valid and return false
        return not stack