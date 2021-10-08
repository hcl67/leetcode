'''
https://leetcode.com/problems/implement-trie-prefix-tree/
'''
class Trie:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        d = self.d
        for c in word+'Z':
            if c not in d:
                d[c] = {}
            d = d[c]
            
    def search(self, word: str) -> bool:
        return self.startsWith(word+'Z')

    def startsWith(self, prefix: str) -> bool:
        d = self.d
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
