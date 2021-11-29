'''
https://leetcode.com/problems/accounts-merge/
'''
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        acc_dict = {}
        for acc in accounts:
            cur_name,cur_eml_set = acc[0],set(acc[1:])
            if cur_name not in acc_dict:
                acc_dict[cur_name] = [cur_eml_set]
            else:
                new_eml = []
                for i in range(len(acc_dict[cur_name])):
                    if len(acc_dict[cur_name][i] & cur_eml_set) > 0:
                        cur_eml_set |= acc_dict[cur_name][i]
                    else:
                        new_eml += [acc_dict[cur_name][i]]
                new_eml += [cur_eml_set]
                acc_dict[cur_name] = new_eml
        ans = []
        for k,v in acc_dict.items():
            for vi in v:
                ans += [[k] + sorted(list(vi))]
        return ans
            
