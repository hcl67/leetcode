'''
https://leetcode.com/problems/complement-of-base-10-integer/
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if n == 0 else (1<<n.bit_length())-1-n
        
