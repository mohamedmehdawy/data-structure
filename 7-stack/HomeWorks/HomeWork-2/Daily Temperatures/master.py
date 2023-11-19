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
        answers = [0] * len(temperatures)
        stack = []
        
        for index, temperature in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temperature:
                prev_index = stack.pop()
                answers[prev_index] = index - prev_index
            stack.append(index)
        return answers              