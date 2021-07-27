'''
https://leetcode.com/problems/3sum-closest/
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bst = sum(nums[:3])
        if bst >= target:
            return bst
        n = len(nums)
        if n == 3:
            return bst
        dff = abs(target - bst)
        for i in range(n-2):
            j = i + 1
            k = n - 1
            innertgt = target - nums[i]
            innerbst = nums[j] + nums[k]
            innerdff = abs(innertgt - innerbst)
            while k > j:
                innersum = nums[j] + nums[k]
                if innersum == innertgt:
                    return target
                if abs(innertgt - innersum) < innerdff:
                    innerbst = innersum
                    innerdff = abs(innertgt - innerbst)
                if innersum > innertgt:
                    k -= 1
                else:
                    j += 1
            if abs(nums[i] + innerbst - target) < dff:
                bst = nums[i] + innerbst
                dff = abs(nums[i] + innerbst - target)
            if j == i+1 and k == j+1 and bst >= target:
                return bst
        return bst
                
        
