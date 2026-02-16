class Solution:
    def commonElements(self, arr1, arr2, arr3):

        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i = j = k = 0
        result = []
        
        while i < n1 and j < n2 and k < n3:
            if arr1[i] == arr2[j] == arr3[k]:
            
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                
                min_val = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == min_val:
                    i += 1
                if arr2[j] == min_val:
                    j += 1
                if arr3[k] == min_val:
                    k += 1
        
        return result if result else [-1]
