class Solution:
    def findMedian(self, arr):
        arr.sort()
        n = len(arr)
        mid = n // 2
        
        if n % 2 == 0:
        
            median = (arr[mid - 1] + arr[mid]) / 2
        else:
        
            median = arr[mid]
        
        return median
