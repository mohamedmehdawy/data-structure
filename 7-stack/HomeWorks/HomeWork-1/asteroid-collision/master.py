class Solution(object):
    


    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # if has one element return the list
        
        if len(asteroids) < 2:
            return asteroids
        
        # create the stack
        stack = []
        
        # start check asteroids
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        
        
        return stack
    