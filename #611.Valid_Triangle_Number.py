'''
https://leetcode.com/problems/valid-triangle-number/
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        import bisect

        ans = 0
        nums = sorted(nums)
        pos1 = bisect.bisect_right(nums,0)
        for a in range(pos1,len(nums)-2):
            lastc = a+2
            for b in range(a+1,len(nums)-1):
                posc = bisect.bisect_left(nums[lastc:],nums[a]+nums[b])
                ans += posc + lastc - b - 1
                lastc += posc

        return ans
        
'''
        ans = 0
        nums = sorted(nums)
        n = len(nums)
        a = n-2
        for c in range(n-1,1,-1):
            while(1):
                if a < 0:
                    a = 0
                    break
                if nums[a] + nums[a+1] > nums[c]:
                    a -= 1
                else:
                    a += 1
                    break
            if a >= c - 1:
                continue
            ans += (c-a) * (c-a-1) // 2
            for i in range(a):
                b = bisect.bisect_right(nums[i+2:c],nums[c]-nums[i])
                ans += c-b-i-2

        
        return ans
            

        ans = 0
        nums = sorted(nums)
        for a in range(len(nums)-2):
            for b in range(a+1,len(nums)-1):
                posc = bisect.bisect_left(nums[b+1:],nums[a]+nums[b])
                ans += posc

        return ans
'''
