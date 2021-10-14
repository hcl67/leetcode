'''
https://leetcode.com/problems/perfect-squares/
'''
class Solution:
    def numSquares(self, n: int) -> int:
        
        sqlst = [x**2 for x in range(1,101)]

        ml = {n}
        m = 0
        while 1:
            newml = set()
            m += 1
            for k in ml:
                if k in sqlst:
                    return m
                else:
                    for i in sqlst:
                        if i > k:
                            break
                        newml.add(k - i)
            ml = newml

            
    
        
