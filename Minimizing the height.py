class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        arr.sort()
        
        ans = arr[-1] - arr[0]
        
        small = arr[0] + k
        large = arr[-1] - k
    
        if small > large:
            small, large = large, small
        
        for i in range(n - 1):
            if arr[i + 1] - k < 0:
                continue
            
            min_height = min(small, arr[i + 1] - k)
            max_height = max(large, arr[i] + k)
            
            ans = min(ans, max_height - min_height)
        
        return ans
