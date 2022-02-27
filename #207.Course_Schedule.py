'''
https://leetcode.com/problems/course-schedule/
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        od = defaultdict(list)
        il = [0] * numCourses
        for pre in prerequisites:
            od[pre[0]].append(pre[1])
            il[pre[1]] += 1
        cl = [c for c in range(numCourses) if il[c] == 0 ]
        while cl:
            c = cl.pop()
            for oc in od[c]:
                il[oc] -= 1
                if il[oc] == 0:
                    cl.append(oc)
        return max(il) == 0
            
            
            
        
