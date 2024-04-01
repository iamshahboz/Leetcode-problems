'''
Given an integer array nums, return all triplets [num[i], num[j], num[k]] such that
i!=j  i !=k  j!=k and nums[i] + nums[j] + nums[k] == 0

Input [-1, 0, 1, 2, -1, -4]
Output [[-1, -1, 2], [-1, 0, 1]] 

Input [0, 1, 1]
Output []

Input [0,0,0]
Output [0,0,0]

Note that the solution set must not contain duplicate triplets



''' 


import timeit


# this solution has O(n^3)

# def findTriplets(arr):
#     triplets = set()
#     found = False
#     for i in range(0, len(arr)):
#         for j in range(i+1, len(arr)):
#             for k in range(j+1, len(arr)):
#                 if arr[i] + arr[j] + arr[k] == 0:
#                     triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
#                     triplets.add(triplet)
#                     found = True
                    
#     if found:
#         return [list(triplet) for triplet in triplets]
#     else:
#         return []

# arr =     
# execution_time = timeit.timeit(lambda: findTriplets(arr), number=400)
# print(findTriplets(arr))
# print(execution_time)

# here is the better approach

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []

        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left +1]:
                        left += 1 
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0: 
                    left += 1
                else:
                    right -= 1
        
        return triplets
    
nums = [-2,3,7,0,1,1,3,-1,-1,2,-4,2,1,1,5,-3,4]
solution = Solution()
print(solution.threeSum(nums))

    




