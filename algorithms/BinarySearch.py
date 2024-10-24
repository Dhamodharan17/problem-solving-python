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
        

        
