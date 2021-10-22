'''
https://leetcode.com/problems/sort-characters-by-frequency/
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        charsort = sorted(counter.keys(), key=lambda x:counter[x], reverse = True)
        return ''.join([x * counter[x] for x in charsort])
        
