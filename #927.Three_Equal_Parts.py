'''
https://leetcode.com/problems/three-equal-parts/
'''

#搜索的方案还不够好，把1一切三后搜索比较位数更快
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        def n0d(l):
            i = 0
            n = len(l)
            while(i < n and l[i] == 0):
                i+=1
            return n - i
        i = 0
        n = len(arr)
        j = n - 1
        sub1 = arr[:i+1]
        sub2 = arr[i+1:j]
        sub3 = arr[j:]
        n1 = n0d(sub1)
        n2 = n0d(sub2)
        n3 = n0d(sub3)
        if n1 == 0 and n2 == 0 and n3 == 0:
            return [i,j]
        elif n2 == 0:
            return [-1,-1]
        elif n1 + n2 + n3 <3:
            return [-1,-1]
        else:   #初始化
            if n1 == 0:
                while(arr[i] == 0):
                    i += 1
                n1 = 1
                n2 = n0d(arr[i+1:j])
            if n3 == 0:
                while(arr[j] == 0):
                    j -= 1
                n3 = n - j
                n2 -= n3 - 1
            while(i+1<j):
                if n2 < n1 or n2 < n3:
                    return [-1,-1]
                elif n1 < n3:
                    i += 1
                    n1 += 1
                    if arr[i] != 0:
                        n2 = n0d(arr[i+1:j])
                elif n1 > n3:
                    j -= 1
                    n2 -= 1
                    n3 += 1
                    while(arr[j] == 0):
                        j -= 1
                        n2 -= 1
                        n3 += 1
                elif n1 == n3 and n1 < n2:
                    j -= 1
                    n2 -= 1
                    if arr[j] != 0:
                        n3 = n - j
                elif n1 == n3 and n2 == n3:
                    sub1 = arr[:i+1]
                    sub2 = arr[i+1:j]
                    sub3 = arr[j:]                    
                    for k in range(n3):
                        if sub1[-1-k] != sub2[-1-k] or sub1[-1-k] != sub3[-1-k]:
                            return [-1,-1]
                    return [i,j]
                else:
                    return [-1,-1]
            return [-1,-1]   
                
            
                
        
        
'''        
        def bl2d(l):
            d = 0
            for i in l:
                d *= 2
                d += i
            return d
        i = 0
        j = n = len(arr) - 1
        sub1 = arr[i]
        sub3 = arr[j]
        while(i+1<j):
            if sub1 == sub3:
                sub2 = bl2d(arr[i+1:j])
                if sub1 == sub2:
                    return [i,j]
                else:
                    j -= 1
                    while(sub3 == 0 and arr[j] == 0 and j > 0):
                        j -= 1                    
                    sub3 += arr[j] * 2**(n-j)
            elif sub1 > sub3:
                j-=1
                while(arr[j] == 0 and j > 0):
                    j -= 1
                sub3 += arr[j] * 2**(n-j)
            else:
                if sub1 == 0:
                    while(arr[i] == 0 and i < n):
                        i += 1
                    sub1 = arr[i]
                else:
                    i+=1
                    sub1 *= 2
                    sub1 += arr[i]
        return [-1,-1]
'''
