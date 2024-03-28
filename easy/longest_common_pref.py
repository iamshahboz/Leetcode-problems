'''
Write a function to find the longest prefix string amongs an array of
strings. If there is no common prefix return an empty array

input: strs= ['flower','flow','flight']
output: 'fl'

input: strs= ['dog','racerar','car']
output: ''
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if (i==len(word) or word[i] != base[i]):
                    return base[0:i]
        return base 
solution = Solution()
strs = ['apple','application','apointment','append']
result = solution.longestCommonPrefix(strs)
print(result)

