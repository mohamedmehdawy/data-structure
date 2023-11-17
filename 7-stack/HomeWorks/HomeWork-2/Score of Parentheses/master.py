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
        # stack will have [Boolean: for multi by 2, value: the value of the paranthese]
        stack = []
        score = 0
        
        for char in s:
            if char == "(":
                if stack and not stack[-1][0]:
                    last_element = stack[-1]
                    last_element[0] = True
                    last_element[1] = 0
                stack.append([False, 1])

            else:
                last_element = stack[-1]
                if not last_element[0] and len(stack) > 1:
                    stack[-2][1] += last_element[1]
                elif last_element[0] and len(stack) > 1:
                    stack[-2][1] += last_element[1] * 2
                else:
                    if last_element[0]:
                        
                        score += last_element[1] * 2
                    else:
                        score += last_element[1]
                stack.pop()
                    
        return score