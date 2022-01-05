'''
https://leetcode.com/problems/palindrome-partitioning/
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def _isp(s):
            return len(s)==1 or s==s[::-1]
        ans = []
        q = deque([[s]])
        while q:
            cur = q.pop()
            lst = cur[-1]
            #print(cur)
            if _isp(lst):
                ans.append(cur)
            for i in range(1,len(lst)):
                if _isp(lst[:i]):
                    #print(cur[:-1]+[lst[:i],lst[i:]])
                    q.append(cur[:-1]+[lst[:i],lst[i:]])
        return ans
            
