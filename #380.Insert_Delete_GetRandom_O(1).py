'''
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
# 看了答案提示后的代码
class RandomizedSet:
    from random import choice

    def __init__(self):
        self.d = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        else:
            self.d[val] = len(self.d)
            self.l += [val]
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.s:
            i = self.d[val]
            v = list[-1]
            l[i],l[-1] = l[-1],l[i]
            self.d[v] = i
            del self.d[val]
            self.l.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return choice(self.l)
        


# 其实不满足题目要求
'''
class RandomizedSet:
    from random import choice

    def __init__(self):
        self.s = set()
        

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        else:
            self.s.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return choice(list(self.s))
        
 '''       


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
