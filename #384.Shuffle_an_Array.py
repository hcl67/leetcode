'''
https://leetcode.com/problems/shuffle-an-array/
'''
class Solution:
    import random

    def __init__(self, nums: List[int]):
        self.ori = [i for i in nums]
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.ori
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return sorted(self.ori,key=lambda x:random.random())
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
