class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)

        #pick and unpick since at any stage, value can increase and decrease
        def util(current_index, prev):

            if current_index < 0:
                return 0 # no more elements

            pick = 0
            if prev == -1 or nums[current_index] < nums[prev]:
                pick = 1 + util(current_index-1,current_index)
           
            skip = util(current_index-1,prev)

            return max(pick, skip)
        
        return util(n-1,-1)


#top down
#bigger problem - find lis of set, length n
#smaller problem ->  find lis of set, length n-1
#when we are reducing the problem size, prev will change
#also we need to try all possible ways
class Solution(object):
    def lengthOfLIS(self, nums):
        
        n = len(nums)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]

        def util(prev, current):

            if current == len(nums):
                return 0
            
            if dp[current][prev+1] != -1:
                return dp[current][prev+1]

            pick = 0
            if prev == -1 or nums[current] > nums[prev]:
                # prev will change since we are continuing seq
                pick = 1 + util(current, current+1)

            skip = util(prev, current+1)

            #both moves next element, prev matters
            dp[current][prev+1] = max(pick, skip)
            return dp[current][prev+1]
        
        return util(-1, 0)

#bottom up
class Solution(object):
    def lengthOfLIS(self, nums):

        n = len(nums)
        dp =[ [0 for _ in range(n+1)] for _ in range(n+1)]

        # LIS for empty array
        for i in range(n+1):
            dp[n][i] = 0

        for cur in range(n-1, -1, -1):
            for prev in range(cur-1,-2,-1):

                not_take = dp[cur+1][prev+1]#prev since -1 , +1

                take = 0
                if prev == -1 or nums[cur] > nums[prev]:
                    take = 1 + dp[cur+1][cur+1]#cur

                dp[cur][prev+1] = max(take, not_take)

        return dp[0][0]

       
        



