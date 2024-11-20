class Solution(object):
    def largestDivisibleSubset(self, nums):
        
        n = len(nums)
        nums.sort()
        dp = [ 1 for _ in range(n)]
        hash = [ i for i in range(n)]

        for cur in range(n):
            for prev in range(cur):
                if nums[cur] % nums[prev] == 0:
                    if dp[cur] < dp[prev]+1:
                        dp[cur] = dp[prev]+1
                        hash[cur] = prev
        # find end
        ans = -1
        last_index = -1

        for i in range(n):
            if dp[i] > ans:
                ans = dp[i]
                last_index  = i
        # trace back
        list=[]
        list.append(nums[last_index])
        while hash[last_index] != last_index:
            last_index = hash[last_index]
            list.append(nums[last_index])
            

        list.reverse()
        return list

        
        

        
