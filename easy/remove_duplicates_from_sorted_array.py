
'''
Given the array, the function should loop through the array 
and delete the duplicated element from the list
at the end it should return the number of unique elements 
'''

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        
        return index + 1

solution = Solution()
nums = [1,1,2]
result = solution.removeDuplicates(nums)
print(result)