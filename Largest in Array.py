class Solution:
    def largest(self, arr):
        largest_element = arr[0]
        
        for num in arr:
            if num > largest_element:
                largest_element = num
                
        return largest_element
