class Solution:
    def median(self, mat):
        import bisect
        
        n = len(mat)
        m = len(mat[0])
        total = n * m
        desired = total // 2 + 1
        
        min_val = min(row[0] for row in mat)
        max_val = max(row[-1] for row in mat)
        
        while min_val < max_val:
            mid_val = (min_val + max_val) // 2
            
            count = 0
            for row in mat:
                count += bisect.bisect_right(row, mid_val)
            
            if count < desired:
                min_val = mid_val + 1
            else:
                max_val = mid_val
        
        return min_val
