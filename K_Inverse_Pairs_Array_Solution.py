class Solution:
#    from math import perm,comb
    def kInversePairs(self, n: int, k: int) -> int:
# trail 3正向构造
        nk = [[0] * (k+1) for i in range(n+1)]
        nk[1][0] = 1
        for i in range(2,n+1):
            tmp = 0
            for j in range(k+1):
                if j-i+1 <= 0:
                    tmp += nk[i-1][j]
                else:
                    tmp = tmp + nk[i-1][j] - nk[i-1][j-i]
                nk[i][j] = tmp
                if nk[i][j] >10**9 + 7:
                    nk[i][j] = nk[i][j]%(10**9 + 7)
#        print(nk)
        return nk[n][k]
                
                
                
    


'''

#trial 2
        sum = 0
        if k == 0:
            return 1
        elif k > n*(n-1)/2:
            return 0
        elif k == n*(n-1)/2:
            return 1
        elif n > k:
            for i in range(k+1):
                sum += self.kInversePairs(k, k-i) * comb(n-k+i-1, i)
        else:
            for i in range(min(k+1,n)):
                sum += self.kInversePairs(n-1, k-i)
        
        if sum >10**9 + 7:
            return sum%(10**9 + 7)
        else:
            return sum


#trial 1
        sum = 0
        if k == 0:
            return 1
        elif k > n*(n-1)/2:
            return 0
        elif k == n*(n-1)/2:
            return 1
        for i in range(min(k+1,n)):    #注意每次到n最多只能增加n-1个逆对，递归中下一轮的k不能小于当前的k-(n-1)，即i最大到n-1(含)
            print(n-1, k-i)
            sum += self.kInversePairs(n-1, k-i)
        if sum >10**9 + 7:
            return sum%(10**9 + 7)
        else:
            return sum
'''      
    
        
'''
从1开始增加，每次增加到第t位数字时，可以在之前的逆序对上增加产生1~t种新的逆序对

例如
1
0

12                       21 
0                        1 

(12)123  132  312       (21) 213   231  321
    0    1     2             1     2    3

(123)1234 1243 1423 4123  
     0    1    2    3 

(132)1324 1342 1432 4132
     1    2    3    4

(312)3124 3142 3412 4312
     2    3    4    5

(213)2134 3243 2413 4213  
     1    2    3    4 

(231)2314 2341 2431 4231
     2    3    4    5

(321)3214 3241 3421 4321
     3    4    5    6
          
     
     
     
     
     

问题转化为
sum(i = 1 -> n) t(i) = k 的个数 其中 t(i)表示[1,i)的数

问题进而转化为 n-k如何在1~n中分配，即某种带约束的插隔板问题？

尝试1，试图通过递归求解，速度太慢



尝试解析解 问题等价于n个盒子，大小从1~n 放k个球

0|00|000 3个盒子中放入4个球，有 121,112,103,022,013 5种方法

尝试2，考虑对大于等于球的个数的盒子和小于球的个数的盒子分开判断，大于球个数的盒子即不用考虑盒子放满的问题，即在n个盒子里放k个球 = c(k+n-1,k).当k大时依旧速度慢

尝试3，正向构造



'''
