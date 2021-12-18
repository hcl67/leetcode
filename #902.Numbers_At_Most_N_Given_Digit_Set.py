'''
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
'''
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        strn = str(n)
        lenn = len(strn)
        if lenn == 1:
            return len([x for x in digits if x <= strn])
        ans = 0
        for i in range(1,lenn):
            ans += len(digits)**(lenn-i)
        for i in range(lenn):
            ans += len([x for x in digits if x < strn[i]]) * len(digits) ** (lenn-i-1)
            if strn[i] not in digits:
                break
        else:
            ans += 1
        return ans
        
        
