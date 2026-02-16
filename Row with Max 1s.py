class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        if n == 0:
            return -1
        m = len(arr[0])
        max_row_index = -1
        
        i, j = 0, m - 1
        
        while i < n and j >= 0:
            if arr[i][j] == 1:
            
                max_row_index = i
                j -= 1
            else:
            
                i += 1
        
        return max_row_index
