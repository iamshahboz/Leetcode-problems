'''
Given sorted array of distinct integers and target value, return the index if the target
is found. If not return the index where it would be if we were inserted in order

Input nums = [1,3,5,6] target=5
Output 2

Input nums = [1,3,5,6] target=7
Output 4


'''

class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return (nums.index(target))
        else:
            for i in range(0,len(nums)):
                found = False
                if nums[i] > target:
                    index = nums.index(nums[i])
                    return index
        return len(nums)
    
solution = Solution()
nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target))

# this solution is running is O(n) time complexity

