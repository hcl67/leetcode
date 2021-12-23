'''
https://leetcode.com/problems/course-schedule-ii/
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(numCourses))
        inddict = defaultdict(int)
        outdict = defaultdict(set)
        for pre in prerequisites:
            inddict[pre[0]] += 1
            outdict[pre[1]].add(pre[0])
        que = deque(list(set(range(numCourses)) - set(inddict.keys())))
        don = []
        while que:
            nod = que.popleft()
            don.append(nod)
            for j in outdict[nod]:
                inddict[j] -= 1
                if inddict[j] == 0:
                    que.append(j)
        if len(don) == numCourses:
            return don
        else:
            return []
            
