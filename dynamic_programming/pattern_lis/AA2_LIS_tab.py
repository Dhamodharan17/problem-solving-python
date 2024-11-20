class Solution(object):
    def lengthOfLIS(self, nums):
        
        n = len(nums)
        #dp[i] - LIS possible end with element at nums[i]
        dp =[1 for _ in range(n)]
        maxi = -1

        for i in range(n):
            # for each element, check all its prev
            # decide to join the best
            for prev in range(i):
                if nums[prev] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[prev])
                    maxi = max(maxi,dp[i])
        
        return maxi if maxi != -1 else 1
