class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Choose number
                path.append(candidates[i])
                
                # Move to next index (i+1) since we can't reuse same element
                backtrack(i + 1, remaining - candidates[i], path)
                
                # Backtrack
                path.pop()
        
        backtrack(0, target, [])
        return result
