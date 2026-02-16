class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        count = sum(1 for x in arr if x <= k)
        
        if count == 0:
            return 0
        
        bad = sum(1 for x in arr[:count] if x > k)
        min_swaps = bad
        
        for i in range(1, n - count + 1):
        
            if arr[i - 1] > k:
                bad -= 1
        
            if arr[i + count - 1] > k:
                bad += 1
            
            min_swaps = min(min_swaps, bad)
        
        return min_swaps
