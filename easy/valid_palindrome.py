'''
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 
Input: s = "A man, a plan, a canal: Panama"
Output: False
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = 'race a car'
Output: False
Explanation: "raceacar" is not a palindrome

'''

import re 

class Solution(object):
    def isPalindrome(self, s):
        result = s.lower().replace(' ', '')
        more = re.sub('[^0-9a-zA-Z]+', '', result)
        reverse = more[::-1]
        if more != reverse:
            return False 
        else:
            return True 
        
s = "A man, a plan, a canal: Panama"
my_result = Solution()
print(my_result.isPalindrome(s))
