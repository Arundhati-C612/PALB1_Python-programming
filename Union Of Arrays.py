class Solution:    
    def findUnion(self, a, b):
        union_set = set(a)
        
        for num in b:
            union_set.add(num)
        
        return list(union_set)
