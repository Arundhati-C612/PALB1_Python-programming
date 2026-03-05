class Solution(object):
    def searchRange(self, nums, target):
        
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1   # move left
                    else:
                        left = mid + 1    # move right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return bound
        
        first = findBound(True)
        if first == -1:
            return [-1, -1]
        
        last = findBound(False)
        return [first, last]
