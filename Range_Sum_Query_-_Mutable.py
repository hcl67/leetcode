class NumArray:
    
    l = []
    lastsum = 0
    lastright = -1
    lastleft = -1
    
    def __init__(self, nums: List[int]):
        self.l = nums
#        print(self.l)
        

    def update(self, index: int, val: int) -> None:
#        print(self.l)
        if index >= self.lastleft and index < self.lastright + 1:
            self.lastsum += (val - self.l[index])
        self.l[index] = val
#        print(self.l, index, val)
        
        

    def sumRange(self, left: int, right: int) -> int:
#        print(self.l,self.lastsum, self.lastleft,self.lastright, left, right)
        if self.lastleft > -1 and (abs(left - self.lastleft) + abs(right - self.lastright)) < (right - left):
            if left > self.lastleft:
                leftsum = sum(self.l[self.lastleft:left]) * -1
            elif left == self.lastleft:
                leftsum = 0
            else:
                leftsum = sum(self.l[left:self.lastleft])
            if right > self.lastright:
                rightsum = sum(self.l[self.lastright+1:right+1])
            elif right == self.lastright:
                rightsum = 0
            else:
                rightsum = sum(self.l[right+1:self.lastright+1]) * -1
            s = self.lastsum + leftsum + rightsum
        else:
            s = sum(self.l[left:(right+1)])
        self.lastsum = s
        self.lastleft = left
        self.lastright = right
        return s


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
