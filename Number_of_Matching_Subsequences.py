class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

#子序列DP匹配，预处理，构造查询矩阵，trxm[i][j] 表示从原字符串第i位（含）开始，第一次发现字符j的位置
        lenstr = len(s)
        trxm = [[-1]*26 for i in range(lenstr+1)]
        for i in range(lenstr-1,-1,-1):
            for j in range(26):
                if s[i] == chr(j+97):
                    trxm[i][j] = i
                else:
                    trxm[i][j] = trxm[i+1][j]
#        print(trxm)
        kn = 0
        for w in words:
#            print(w)
            nextl = 0
            for l in w:
                nextl = trxm[nextl][ord(l)-97]  #查看下一位字符的位置
#                print(nextl)
                if nextl >= 0:
                    nextl += 1    #下次查找下一位字符的位置+1开始
                else:
                    break
            if nextl >= 0:
                kn += 1
        return kn
                
                

        
        
        
        
'''
#子序列双指针匹配，速度不够快，改用DP匹配        
        lenwords = len(words)
        leneachword = [len(i_w) for i_w in words]
        checkwords = [0] * lenwords
        checkwordsl = [i_w[0] for i_w in words]
        kn = 0
        for i_s in s:
            for j in range(lenwords):
                if checkwords[j] >= 0 and checkwordsl[j] == i_s:
                    checkwords[j] += 1
                    if checkwords[j] == leneachword[j]:
                        checkwords[j] = -1
                        kn += 1
                    else:
                        checkwordsl[j] = words[j][checkwords[j]]
#            print(i_s)
#            print(checkwords)
            if kn == lenwords:
                break
        return kn
'''        
