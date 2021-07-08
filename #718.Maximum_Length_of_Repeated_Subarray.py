'''
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        match = [[0 for j in range(len2)] for i in range(len1)]
        for i in range(len1):
            for j in range(len2):
                if nums1[i] == nums2[j]:
                    if i> 0 and j>0:
                        match[i][j] = match[i-1][j-1] + 1
                    else:
                        match[i][j] = 1
        return max([max(match[i]) for i in range(len1)])
