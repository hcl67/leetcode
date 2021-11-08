'''
https://leetcode.com/problems/unique-binary-search-trees/
'''
class Solution:
    def numTrees(self, n: int) -> int:
        #即求n个节点可以构成多少种二叉树，N(0) = 1 N(n) = sum(i=0->n-1)N(i)N(n-1-i)
        '''
        f=[1]
        for _ in range(n):
            f += [sum(f[i]*f[len(f)-1-i] for i in range(len(f)))]
        #print(f)
        return f[-1]
        '''
        #A000108		Catalan numbers: C(n) = binomial(2n,n)/(n+1) = (2n)!/(n!(n+1)!).
        return math.comb(2*n,n)//(n+1)
        
