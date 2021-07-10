class Solution:
    def numDecodings(self, s: str) -> int:

# trial 2，经过网络解法提示，利用递推公式 s[n] = decode(s[-2:])*s[n-2] + decode(s[-1:])*s[n-1]

        modd = 10**9 + 7
        def decode1(s): #1位数字
            if s == '0':
                return 0
            elif s == '*':
                return 9
            else:
                return 1
        
        def decode2(s):  #2位数字
            if s[0] == '0':
                return 0
            elif s[0] == '1':
                if s[1] != '*':
                    return 1
                else:
                    return 9
            elif s[0] == '2':
                if s[1] in {'0','1','2','3','4','5','6'}:
                    return 1
                elif s[1] == '*':
                    return 6
                else:
                    return 0
            elif s[0] == '*':
                if s[1] in {'0','1','2','3','4','5','6'}:
                    return 2
                elif s[1] in {'7','8','9'}:
                    return 1
                elif s[1] == '*':
                    return 15
            else:
                return 0
            
        cnt = [1]
        cnt += [decode1(s[0])]
        for i in range(2,len(s)+1):
            cnt += [(cnt[-2] * decode2(s[i-2:i]) + cnt[-1] * decode1(s[i-1:i])) % modd]
        return cnt[-1]
        
        
        

'''     
#trial 1 超时，不能解决*****的问题
        
        def rdecoding(s):
            if len(s) == 0:
                return 1
            elif s[0] == '0':
                return 0
            elif len(s) == 1 and s!='*':
                return 1
            elif len(s) == 1 and s=='*':
                return 9
            elif s[0] in {'3','4','5','6','7','8','9'}:
                return rdecoding(s[1:])
            elif s[:2] in {'27','28','29','20','10'}:
                return rdecoding(s[2:])
            elif s[:2] in {'23','24','25','26','13','14','15','16','17','18','19'}:
                return 2 * rdecoding(s[2:])
            elif s[:2] in {'12','22','11','21'}:
                return rdecoding(s[1:]) + rdecoding(s[2:])
            elif s[:2] == '2*':
                return rdecoding('22'+s[2:]) + rdecoding('21'+s[2:]) + 11 * rdecoding(s[2:])
            elif s[:2] == '1*':
                return rdecoding('12'+s[2:]) + rdecoding('11'+s[2:]) + 14 * rdecoding(s[2:])
            elif s[:2] in {'*0'}:
                return 2 * rdecoding(s[2:])
            elif s[:2] in {'*9','*8','*7'}:
                return 10 * rdecoding(s[2:])
            elif s[:2] in {'*6','*5','*4','*3'}:
                return 11 * rdecoding(s[2:])
            elif s[:2] in {'*2','*1'}:
                return 9 * rdecoding(s[1:]) + 2 * rdecoding(s[2:])
            elif s[:2] == '**':
                return 78 * rdecoding(s[2:]) + 9 * rdecoding('1'+s[2:]) + 9 * rdecoding('2'+s[2:])
            else:
                return 0
        subs = ''
        ans = 1
        for c in s:
            if c in {'3','4','5','6','7','8','9','0'}:
                subs += c
                ans *= rdecoding(subs)%(10**9 + 7)
                subs = ''
            else:
                subs += c
        ans *= rdecoding(subs)%(10**9 + 7)
                
        return ans%(10**9 + 7)
'''        
              
        
