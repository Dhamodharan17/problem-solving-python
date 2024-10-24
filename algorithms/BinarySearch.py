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

        
