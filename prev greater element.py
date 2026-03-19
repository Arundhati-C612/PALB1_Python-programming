class Solution:
    def preGreaterEle(self, arr):
        stack = []
        res = []

        for x in arr:
            # Remove elements smaller or equal to current
            while stack and stack[-1] <= x:
                stack.pop()
            
            # Assign result
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            
            # Push current element
            stack.append(x)
        
        return res
