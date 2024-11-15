#recursion
class Solution(object):
    def canPartition(self, nums):
        total_sum = sum(nums)
        n = len(nums)
        
        if total_sum % 2 != 0:
            return False
        
        def util(current_index, current_target):

            if current_index == 0:
                return nums[0] == current_target
            
            pick = False
            if nums[current_index] <= current_target:
                pick = util(current_index-1, current_target - nums[current_index])

            skip = util(current_index-1, current_target)

            return pick or skip
        
        return util(n-1,total_sum/2)

#top down
class Solution(object):
    def canPartition(self, nums):

        total_sum = sum(nums)
        n = len(nums)

        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum / 2

        dp = [[0 for _ in range(target_sum+1)] for _ in range(n)]

        # All sets can for sum 0
        for i in range(n):
            dp[i][0] = True
        
        if nums[0] <= target_sum:
            dp[0][nums[0]] = True

        for i in range(1, n):
            for j in range(1, target_sum+1):
                
                include = False
                if nums[i] <= target_sum:
                    include = dp[i-1][target_sum - nums[i]]
                exclude = dp[i-1][target_sum]

                dp[i][j] = include or exclude
        
        return dp[n-1][target_sum]

#space
class Solution(object):
    def canPartition(self, nums):

        total_sum = sum(nums)
        n = len(nums)

        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum / 2

        prev = [0 for _ in range(target_sum+1)]
        prev[0] = True
        
        if nums[0] <= target_sum:
            prev[nums[0]] = True

        for i in range(1, n):
            current = [0 for _ in range(target_sum+1)]
            current[0] = True
            for j in range(1, target_sum+1):
                
                include = False
                if nums[i] <= target_sum:
                    include = prev[target_sum - nums[i]]
                exclude = prev[target_sum]

                prev[j] = include or exclude
        
        return prev[target_sum]
        
