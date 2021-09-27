'''
https://leetcode.com/problems/unique-email-addresses/
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for e in emails:
            el,em  = e.split('@')
            ul = ''
            for c in el:
                if c == '.':
                    continue
                elif c == '+':
                    break
                else:
                    ul += c
            ans.add(ul + '@' + em)
        return len(ans)
        
