'''
https://leetcode.com/problems/next-greater-element-i/
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n1 in nums1:
            i = nums2.index(n1) 
            r = -1
            for j in range(i, len(nums2)):
                if nums2[j] > n1:
                    r = nums2[j]
                    break
            ans += [r]
        return ans
        
