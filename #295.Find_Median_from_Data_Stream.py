'''
https://leetcode.com/problems/find-median-from-data-stream/
'''
class MedianFinder:
    import bisect
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.orderlist = []
        self.lenn = 0
        
        

    def addNum(self, num: int) -> None:
        self.orderlist.insert(bisect.bisect_left(self.orderlist,num),num)
        self.lenn += 1

    def findMedian(self) -> float:
        if self.lenn %2 == 1:
            return self.orderlist[self.lenn//2]
        else:
            return (self.orderlist[self.lenn//2-1]+self.orderlist[self.lenn//2])/2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
