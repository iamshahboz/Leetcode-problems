# Given an integer x, return True if x is a Palindrome and False otherwise

# example
'''
x = 121
output: True
Because 121 reads as 121 from left to right and from right to left 
'''

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        n = x[::-1]
        if x == n:
            return True
        else:
            return False 
        
solution = Solution()
x = 788
result = solution.isPalindrome(x)
print(result)
