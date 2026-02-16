class Solution:
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
        
        result = []
        n = len(mat)
        m = len(mat[0])
        
        top, bottom = 0, n - 1
        left, right = 0, m - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right
            for j in range(left, right + 1):
                result.append(mat[top][j])
            top += 1
            
            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # Traverse from right to left, if row still exists
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(mat[bottom][j])
                bottom -= 1
            
            # Traverse from bottom to top, if column still exists
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        
        return result
