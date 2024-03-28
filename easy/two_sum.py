# Given an array of integers nums and an integer target, return indices(indexes)
# of the two numbers such that they add up to target

'''
example
nums = [2,7,11,15]
target = 9

output = [0,1]
because nums[0] + nums[1] == 9
'''

# Solution

class Solution(object):
    def twoSum(self, nums, target):
        indexes = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    indexes.append(i)
                    indexes.append(j)

        return indexes 
        
solution = Solution()
nums = [4,7,3,8,1]
target = 8
result = solution.twoSum(nums,target)
print(result)
