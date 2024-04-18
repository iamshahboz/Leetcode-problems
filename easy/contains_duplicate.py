'''
Given an integer array nums, return True if any value appears at least twice
in the array and return False if every element is distinct

Example

Input: nums = [1, 2, 3, 1]
Output: True

Input: nums = [1, 2, 3, 4]
Output: False
'''
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    unique_set = set()

    for num in nums:
        if num in unique_set:
            return True
        else:
            unique_set.add(num)

    return False 


nums = [2, 4, 5, 2, 8 , 9]
result = containsDuplicate(nums)
print(result)


