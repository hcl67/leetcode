class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
#recursion solution
        
        n = len(num)
        ans = []
        def recurse(i, s, leading):
            if i > n-1:
                if eval(s) == target:
                    ans.append(s)
                return
            
            if leading != '0':
                recurse(i+1, s+num[i], leading)
            recurse(i+1, s+"+"+num[i], num[i])
            recurse(i+1, s+"-"+num[i], num[i])
            recurse(i+1, s+"*"+num[i], num[i])
            
        recurse(1, num[0], num[0])
        
        return ans

        
        '''
        oplist = [num[0]]
        for i in range(1,len(num)):
            newoplist = []
            for ol in oplist:
                j = len(ol)-1
                while j >= 0 and ol[j] == '0':
                    j -= 1
                if j >= 0 and ol[j] not in {'+','-','*'}: 
                    newoplist += [ol+num[i]]
                newoplist += [ol+'+'+num[i]]
                newoplist += [ol+'-'+num[i]]
                newoplist += [ol+'*'+num[i]]
            oplist = newoplist
        ans = []
        for op in oplist: 
            if eval(op) == target:
                ans += [op]
        return ans
        '''        
                
