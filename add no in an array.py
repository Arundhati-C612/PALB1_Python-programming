class Solution:
    def get_Sum(self, n, input):
        total = 0
        for i in range(n):
            total += input[i]
        return total
