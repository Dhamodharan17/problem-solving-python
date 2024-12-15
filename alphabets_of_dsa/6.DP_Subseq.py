class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums) - 1
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        def util(current_index, target):

            if target < 0 or current_index < 0:
                return False
            
            if target == 0:
                return True
            
            pick = util(current_index-1, target - nums[current_index])

            unpick = util(current_index-1, target)

            return pick or unpick
        
        return util(n, target)
