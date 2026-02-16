class Solution:
    def mergeArrays(self, a, b):
        
        import math
        n = len(a)
        m = len(b)
        
        def nextGap(gap):
            if gap <= 1:
                return 0
            return (gap + 1) // 2
        
        gap = n + m
        gap = nextGap(gap)
        
        while gap > 0:

            i = 0
            while i + gap < n:
                if a[i] > a[i + gap]:
                    a[i], a[i + gap] = a[i + gap], a[i]
                i += 1
            
            j = gap - n if gap > n else 0
            i = i if gap <= n else n
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1
            
            if j < m:
                j = 0
                while j + gap < m:
                    if b[j] > b[j + gap]:
                        b[j], b[j + gap] = b[j + gap], b[j]
                    j += 1
            
            gap = nextGap(gap)
