'''
https://leetcode.com/problems/reverse-only-letters/
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i,j = 0,len(s)-1
        h,t = '',''
        let = set(string.ascii_letters)
        while i<j:
            if s[i] not in let:
                h += s[i]
                i += 1
            elif s[j] not in let:
                t = s[j] + t
                j -= 1
            else:
                h += s[j]
                t = s[i] + t
                i += 1
                j -= 1
        if i == j:
            return h+s[i]+t
        else:
            return h+t
