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

#有向图查环
#edge = [a,b]  a->b
        inddict = defaultdict(int)
        outdict = defaultdict(set)
        for edge in edges:
            inddict[edge[1]] += 1
            outdict[edge[0]].add(edge[1])
        que = deque(list(set(range(numNodes)) - set(inddict.keys())))
        don = []
        while que:
            nod = que.popleft()
            don.append(nod)
            for j in outdict[nod]:
                inddict[j] -= 1
                if inddict[j] == 0:
                    que.append(j)
        if len(don) == numCNodes:
            return False
        else:
            return True
            
