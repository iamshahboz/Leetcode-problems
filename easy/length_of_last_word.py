'''
Given a string s, consisting of words and spaces, return the length of the last word
in the string

Input s = "Hello world"
Output 5
Explanation: The last word is "world" which has the length of 5
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        result = len(s.split()[-1])
        return result

solution = Solution()
s = "My football team is Liverpool"
l = solution.lengthOfLastWord(s)
print(l)
