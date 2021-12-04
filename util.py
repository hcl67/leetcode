#Prefix Tree (Trie)

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
              

#Disjoint Set Union
def getdsu(p,dsu):
    if dsu[p] != p:
        dsu[p] = getdsu(dsu[p],dsu)
    return dsu[p]

def undsu(p1,p2,dsu,size):
    p1 = getdsu(p1,dsu)
    p2 = getdsu(p2,dsu)
    if p1 == p2:
        return
    elif size[p1] >= size[p2]:
        dsu[p2] = p1
        size[p1] += size[p2]
        size[p2] = 0
    else:
        dsu[p1] = p2
        size[p2] += size[p1]
        size[p1] = 0
    return
