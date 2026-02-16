class Solution:

    def findMinDiff(self, arr,M):
        N = len(arr)
        if M == 0 or N == 0:
            return 0
        
        if M > N:
            return -1 
        
        arr.sort()  
        
        min_diff = float('inf')
        
        for i in range(N - M + 1):
            diff = arr[i + M - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
