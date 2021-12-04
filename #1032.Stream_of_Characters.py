'''
https://leetcode.com/problems/stream-of-characters/
'''
class StreamChecker:
    

    def __init__(self, words: List[str]):
        self.d = {}
        self.qs = ""
        for word in words:
            d = self.d
            for c in word[::-1]+'.':
                if c not in d:
                    d[c] = {}
                d = d[c]
    
    def query(self, letter: str) -> bool:
        self.qs = letter + self.qs
        d = self.d        
        for c in self.qs:
            if '.' in d:
                return True
            if c not in d:
                return False
            d = d[c]
        else:
            if '.' in d:
                return True
            else:
                return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
