#from the discussion
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        dpdict = defaultdict(int)
        def dp(l, r, k):
            if l > r: return 0            
            while l + 1 <= r and boxes[l] == boxes[l + 1]:  # Increase both `l` and `k` if they have consecutive colors with `boxes[l]`
                l += 1
                k += 1
            if dpdict[(l,r,k)] > 0: return dpdict[(l,r,k)] 
            ans = (k+1) * (k+1) + dp(l+1, r, 0)  # Remove all boxes which has the same with `boxes[l]`
            for m in range(l + 1, r + 1):  # Try to merge non-contiguous boxes of the same color together
                if boxes[l] == boxes[m]:
                    ans = max(ans, dp(m, r, k+1) + dp(l+1, m-1, 0))
            dpdict[(l,r,k)] = ans
            return ans

        return dp(0, len(boxes) - 1, 0)
        
'''
BFS, TLE
def removeBoxes(boxes):
    def simplify(boxes,ans):
        newboxes = [x for x in boxes]
        counter = {}
        for i in range(len(newboxes)):
            b = boxes[i]
            if b not in counter:
                counter[b] = [i,i,1]
            else:
                counter[b][1] = i
                counter[b][2] += 1
        while 1:
            rmlst = [k for k,v in counter.items() if v[1] - v[0] - v[2] + 1 == 0]
            if len(rmlst) == 0:
                break
            for r in rmlst:
                rv = counter[r]
                del counter[r]
                newboxes = newboxes[:rv[0]] + newboxes[rv[1]+1:]
                for k,v in counter.items():
                    if v[0] < rv[0] and v[1] > rv[1]:
                        counter[k][1] -= rv[2]
                    elif v[0] > rv[0]:
                        counter[k][0] -= rv[2]
                        counter[k][1] -= rv[2]
                ans += rv[2]**2        
        return newboxes,ans

    sboxes,ans = simplify(boxes, 0)
    bst = 0
    
    if len(sboxes) == 0:
        return ans

    bl = [(sboxes,ans)]
    while len(bl) > 0:
        curbt,bl = bl[0],bl[1:]
        curb,curans = curbt
        k = 0
        for i in range(1,len(curb)):
            if curb[i] == curb[i-1] and i < len(curb)-1:
                continue
            else:
                if i == len(curb)-1:
                    i += 1
                newb,newans = simplify(curb[:k]+curb[i:],curans+(i-k)**2)
                if len(newb) == 0:
                    bst = max(bst,newans)
                else:
                    bl.append((newb,newans))
                k = i

    return bst            

'''
