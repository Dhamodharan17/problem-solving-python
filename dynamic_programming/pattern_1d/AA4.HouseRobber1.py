# Top Down
class Solution(object):
    # larger problem : max amount can be robbed at all houses
    def rob(self, nums):
        N = len(nums)
        dp = [-1] * N
        def util(nums, n, dp):

            if n < 0:
                return 0
                
            # smaller problem - max amount robbed at last house
            # which is not dependent
            if n == 0:
                return nums[0]
            if dp[n] != -1:
                return dp[n]

            rob = nums[n] + util(nums,n-2,dp)

            skip = util(nums,n-1,dp)

            dp[n] = max(rob, skip)
            return dp[n]

        return util(nums, N-1, dp)

#Bottom Up
class Solution(object):
    # larger problem : max amount can be robbed at all houses
    def rob(self, nums):

        N = len(nums)
        if N == 1:
            return nums[0]

        dp = [0] * N
        dp[0] = nums[0]

        # max can be robbed at house
        dp[1] = max(nums[1],nums[0])

        for i in range(2, N):
            rob = nums[i] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(rob, skip)

        return dp[N-1]
# Space opt
class Solution(object):
    # larger problem : max amount can be robbed at all houses
    def rob(self, nums):

        N = len(nums)
        if N == 1:
            return nums[0]
        # Since we just need 2 houses at back
        # Either to chose or not
        prev2 = nums[0]
        # max can be robbed at house
        prev1 = max(nums[1],nums[0])

        for i in range(2, N):
            rob = nums[i] + prev2
            skip = prev1
            cur = max(rob, skip)
            prev2 = prev1
            prev1 = cur

        return prev1


        
