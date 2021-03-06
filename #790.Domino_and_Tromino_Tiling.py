'''
https://leetcode.com/problems/domino-and-tromino-tiling/
'''
class Solution:
    def numTilings(self, n: int) -> int:

        s = deque([1,1])
        ss = 0
        if n<2:
            return s[n]
        for _ in range(n-1):
            s.append((ss*2+sum(s)) % (10**9+7))
            ss = (ss + s.popleft()) % (10**9+7)
        return s[-1]
        # 用矩阵乘法改写：X =[[1,1,0]] * [[1,1,0],[1,0,1],[2,0,1]]**(n-1)
        '''
        import numpy
        
        from numpy.core.numeric import concatenate, isscalar, binary_repr, identity, asanyarray, dot
        from numpy.core.numerictypes import issubdtype    
        def matrix_power(M, n, mod_val):
            # Implementation shadows numpy's matrix_power, but with modulo included
            M = asanyarray(M)
            if len(M.shape) != 2 or M.shape[0] != M.shape[1]:
                raise ValueError("input  must be a square array")
            if not issubdtype(type(n), int):
                raise TypeError("exponent must be an integer")

            from numpy.linalg import inv

            if n==0:
                M = M.copy()
                M[:] = identity(M.shape[0])
                return M
            elif n<0:
                M = inv(M)
                n *= -1

            result = M % mod_val
            if n <= 3:
                for _ in range(n-1):
                    result = dot(result, M) % mod_val
                return result

            # binary decompositon to reduce the number of matrix
            # multiplications for n > 3
            beta = binary_repr(n)
            Z, q, t = M, 0, len(beta)
            while beta[t-q-1] == '0':
                Z = dot(Z, Z) % mod_val
                q += 1
            result = Z
            for k in range(q+1, t):
                Z = dot(Z, Z) % mod_val
                if beta[t-k-1] == '1':
                    result = dot(result, Z) % mod_val
            return result 
        
        s = numpy.array([1,1,0])
        M = numpy.matrix([[1,1,0],[1,0,1],[2,0,1]])
        return dot(s, matrix_power(M, n-1,10**9+7))[0,0] % (10**9+7)
        '''

