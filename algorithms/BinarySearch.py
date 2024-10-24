## Recursive T(n) = O(log n), S(n) = O(n)
class Solution(object):
    def search(self, nums, target):

        return self.function(nums, 0, len(nums) - 1, target)

    def function(self, nums, left, right, target):

        if left > right:
            return -1

        mid = left + ( right - left)//2

        if(nums[mid] ==target ):
            return mid
        
        if(nums[mid] > target):
            return self.function(nums,left,mid-1,target)
        else:
            return self.function(nums,mid+1,right,target)
            
## Iterative T(n) = O(log n), S(n) = O(1)
class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left+(right-left)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return -1

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

''''


