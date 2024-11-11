class Solution(object):
    def rob(self, input):

        N = len(input)

        if N == 1:
            return input[0]
            
        nums_excluded_1 = input[1:]
        nums_excluded_n = input[:-1]
        def util(nums):
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
        op1 = util(nums_excluded_1)
        op2 = util(nums_excluded_n)

        return max(op1,op2)
        
