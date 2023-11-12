class Solution(object):
    def __init__(self):
        self.open = ["[", "(", "{"]
        self.close = ["]", ")", "}"]
        
    def get_pos(self, currentType, char):
        """
            this function return the position of char insted of the type is open or close
            parameters:
                currentType: use open or close elements
                char: the char will search
            returns:
                the pos or false if not found
        """
        try:
            return currentType.index(char) + 1
        except:
            return False
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check if the length of the string is not have 2 pieces
        if len(s) % 2 != 0:
            return False
        
        # create the stack
        stack = []
        
        for char in s:
            # if the current char is in open append it to the stack
            if self.get_pos(self.open, char):
                stack.append(char)
            # if the current char is close, should be the last element in stack is the open of it
            elif len(stack) and  self.get_pos(self.close, char) == self.get_pos(self.open, stack[-1]):
                stack.pop()
            # return false because this is not valid
            else:
                return False
        
        # if have elments in stack, this is valid and return false
        if len(stack):
            return False
        
        return True