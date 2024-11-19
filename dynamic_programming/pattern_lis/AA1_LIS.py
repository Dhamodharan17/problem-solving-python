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

        
