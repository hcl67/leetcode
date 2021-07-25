'''
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/solution/
'''
class Solution:
    def findIntegers(self, n: int) -> int:
        fab = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]
        s = format(n, 'b')
        ans = 0
        ls = len(s)
        for i in range(ls):
            if s[i] == '1':
                ans += fab[ls-i-1]
                if i < ls-1 and s[i+1] == '1':
                    ans += fab[ls-i-2]
                    break
            if i==ls-1:
                ans +=1
        return ans
        
