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
#smaller problem -> find lis where previous = prev
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





