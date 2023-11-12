class Solution(object):
    def __init__(self):
        self.open_symbols = ["[", "(", "{"]
        self.close_symbols = ["]", ")", "}"]
        
    def get_position(self, currentType, char):
        """
            this function return the position of char insted of the type is open or close
            parameters:
                currentType: use open or close elements
                char: the char will search
            returns:
                the position or -1 if not found
        """
        
        return currentType.index(char) if char in currentType else -1

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
            if char in self.open_symbols:
                stack.append(char)
            # if the current char is close, should be the last element in stack is the open of it
            elif stack and self.get_position(self.close_symbols, char) == self.get_position(self.open_symbols, stack[-1]):
                stack.pop()
            # return false because this is not valid
            else:
                return False
        
        # if have elments in stack, this is valid and return false
        return not stack