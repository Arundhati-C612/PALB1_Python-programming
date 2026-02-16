class Solution:
    
    def isSubset(self, a, b):
        
        freq = {}
        for element in a:
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1
        
        for element in b:
            if element not in freq or freq[element] == 0:
                return False
            freq[element] -= 1  
        
        return True
