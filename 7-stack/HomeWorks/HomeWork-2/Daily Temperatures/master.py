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
        
        for i in range(len(temperatures)):
            status = False
            for j in range(i+1, len(temperatures)):
                if(temperatures[i] < temperatures[j]):
                    status = True
                    break
            
            # check status, if true apppend the difference if not, append 0
            if status:
                answers.append(j - i)
            else:
                answers.append(0)
                
        return answers
    
    
print(Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))