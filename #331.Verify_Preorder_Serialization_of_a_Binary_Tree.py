class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 把序列中的 d,#,# => #，最终二叉树只有一个 #
        
        # 方法3,倒序数#数量,36ms
        n = 0
        ind = len(preorder)
        while 1:
            c = preorder[ind-1]
            if c == '#':
                n += 1
            else:
                n -= 1
            if n < 1:
                return False
            ind = preorder.rfind(',',0,ind)
            if ind == -1:
                break
        if n != 1:
            return False
        return True
        
        
        '''
        # 方法2,队列+栈,121ms
        st = []
        qe = preorder.split(',')
        while 1:
            if len(qe) == 0:
                break
            c,qe = qe[0],qe[1:]
            if c == '#' and len(st) >= 2 and st[-1] == '#' and st[-2] != '#':
                st = st[:-2]
                qe = ['#'] + qe
            else:
                st += [c]
        if len(st) == 1 and st[0] == '#':
            return True
        else:
            return False
        
        # 方法1,字符串替换，63ms
        while 1:
            if preorder[0] == '#':
                if len(preorder) == 1:
                    return True
                else:
                    return False
            ind = preorder.find(',#,#')
            if ind == -1:
                return False                    
            indl = preorder.rfind(',',0,ind)+1
            preorder = preorder[:indl] + '#' + preorder[ind+4:]   
            #print(preorder)
        '''        
