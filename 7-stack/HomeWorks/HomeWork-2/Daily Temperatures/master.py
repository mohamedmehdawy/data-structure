class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # check if empty
        if not temperatures:
            return []
        
        # check if have 1 element
        if len(temperatures) == 1:
            return [0]
        
        # create answers and stack
        answers = []
        stack = []
        
        for index in range(1, len(temperatures)):
            # append answer
            answers.append(0)
            
            # check if the current element is less than the next one  1
            if temperatures[index-1] < temperatures[index]:
                answers[index - 1] = 1
                
            else:
                stack.append(index-1)
                
            # check stack
            while stack and temperatures[stack[-1]] < temperatures[index]:
                answers[stack[-1]] = index - stack[-1]
                stack.pop()
                
                
        # append 0 for last element
        answers.append(0)      
        return answers              