class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                
                # Since we can reuse same element, pass i (not i+1)
                backtrack(i, remaining - candidates[i], path)
                
                # Undo choice (backtrack)
                path.pop()
        
        backtrack(0, target, [])
        return result
