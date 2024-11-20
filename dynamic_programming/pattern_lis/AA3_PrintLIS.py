class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        
        dp =[ 1 for _ in range(N)]
        # stores prev value for current i i.e index = current, value = prev
        hash =[ i for i in range(N)]
        for i in range(N):
            for prev in range(i):# check all prev
                
                if arr[prev] < arr[i]:#increasing 
                    if dp[i] < dp[prev] + 1:
                        dp[i] = dp[prev] + 1
                        hash[i] = prev
        
        # find max - LIS
        ans = -1
        last_index = -1
        for i in range(N):
            if dp[i] > ans:
                ans = dp[i]
                last_index = i
                
        # form sequence
        list = []
        list.append(arr[last_index])
        while hash[last_index] != last_index:
            last_index =  hash[last_index]
            list.append(arr[last_index])
            
        list.reverse()
        return list
