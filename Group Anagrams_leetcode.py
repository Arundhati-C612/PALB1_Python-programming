class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        groups = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())
