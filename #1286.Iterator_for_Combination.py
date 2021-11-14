'''
https://leetcode.com/problems/iterator-for-combination/
'''
class CombinationIterator:

    def scomb(self,n,i):
        if i == 0:
            return ['0' * n]
        if i == n:
            return ['1' * n]
        return ['1'+x for x in self.scomb(n-1,i-1)] + ['0'+x for x in self.scomb(n-1,i)]
    
    def __init__(self, characters: str, combinationLength: int):
        #self.comb = [''.join(x) for x in combinations(characters,combinationLength)]
        self.comb = self.scomb(len(characters),combinationLength)
        self.char = characters        
        self.p = 0
        

    def next(self) -> str:
        self.p += 1
        return ''.join(self.char[i] for i in range(len(self.char)) if self.comb[self.p-1][i] == '1')
        

    def hasNext(self) -> bool:
        return self.p != len(self.comb)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
