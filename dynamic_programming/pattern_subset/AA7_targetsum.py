class Solution(object):
    def findTargetSumWays(self, nums, target):
        
        n = len(nums)
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        # no elements make sum 0 in one way
        dp[0][0] = 1

        for i in range(n+1):
            for cur_sum in range(target+1):
                pick = dp[i-1][cur_sum+num[i]]
                skip = dp[i-1][cur_sum-nums[i]]

            dp[i][cur_sum] = pick + skip

        return dp[n][target]

        def util(i, op):

            if target == op:
                return 1

            if i < 0:
                return 0
            
            pick = util(i-1, op+nums[i])
            skip = util(i-1, op-nums[i])

            return pick + skip
        
        return util( len(nums)-1, target)
