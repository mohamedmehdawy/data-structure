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
            if not stack or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid < 0) or (stack[-1] < 0 and asteroid > 0):
                stack.append(asteroid)
            else:
                
                # convert the asteriod and last element to positive
                last_asteroid = stack[-1]
                positive_asteroid = asteroid
                
                if positive_asteroid < 0: positive_asteroid *= -1
                if last_asteroid < 0 : last_asteroid *= -1
                
                # check if the last element is greater than last asteroid
                if positive_asteroid >= last_asteroid:
                    # add status
                    add_status = True
                    
                    for index in range(len(stack) - 1, -1, -1):
                        if stack[index] > 0 and asteroid > 0 or stack[index] < 0 and asteroid < 0:
                            break
                        elif positive_asteroid < stack[index]: 
                            add_status = False
                            break
                        elif stack[index] != asteroid and positive_asteroid >= stack[index]:
                            if positive_asteroid == stack[index]:
                                add_status = False
                                stack.pop()
                                break
                            stack.pop()
                        


                    # check if can add the asteroid
                    if add_status:
                        stack.append(asteroid)
        
        
        return stack
    