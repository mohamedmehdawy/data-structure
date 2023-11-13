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
                last_asteroid = abs(stack[-1])
                positive_asteroid = abs(asteroid)
                
                
                # check if the last element is greater than last asteroid
                if positive_asteroid >= last_asteroid:
                    # add status
                    add_status = True
                    
                    for index in range(len(stack) - 1, -1, -1):
                        # if asteroid and last element have same sign get out the loop
                        if stack[index] > 0 and asteroid > 0 or stack[index] < 0 and asteroid < 0:
                            break
                        # if the positive_asteroid less than the last element, dont append positive_asteroid
                        elif positive_asteroid < stack[index]: 
                            add_status = False
                            break
                        
                        # if the last element and asteroid not same, and the positive_asteroid is greater than last element
                        elif stack[index] != asteroid and positive_asteroid >= stack[index]:
                            # check first if there are same, remove last element and dont push positive_asteroid
                            if positive_asteroid == stack[index]:
                                add_status = False
                                stack.pop()
                                break
                            stack.pop()
                        


                    # check if can add the asteroid
                    if add_status:
                        stack.append(asteroid)
        
        
        return stack
    