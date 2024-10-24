## for loop
class Solution(object):
    def search(self, nums, target):
       
       for index in range(len(nums)):
            if nums[index] == target:
                 return index

       return -1
      
## while loop

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

        
