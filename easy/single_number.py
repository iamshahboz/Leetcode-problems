'''
Given non empty array of integers nums, every element appears twice except for one.
Find that single one

Input nums = [2, 2, 1]
Output: 1

Input nums= [4, 1, 2, 1, 2]
Output: 4


 one way to achieve is to use bitwise XOR operator. The
 XOR operation has a property such that when you XOR a number with itself 
 it becomes 0. So if you XOR all elements of the list duplicate
 elements will cancel each other and you will be left  with the unique number

'''

# class Solution(object):
#     def singleNumber(self, nums):
#         unique_number = 0
#         for num in nums:
#             unique_number ^= num
#         return unique_number
    
# solution = Solution()
# nums = [4,8,6,9,8,6,4]
# result = solution.singleNumber(nums)
# print(result)

# here is the other method

def find_unique_number(nums):
    num_counts = {}
    
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
   
    for num, count in num_counts.items():
        if count == 1:
            return num

# Example usage
numbers = [4, 2, 3, 2, 4, 3, 1]
unique = find_unique_number(numbers)
print(unique)


