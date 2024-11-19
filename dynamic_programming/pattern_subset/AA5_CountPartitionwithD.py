class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        
        total_sum = sum(arr)
        MOD = 10**9+7
      
        #edge case
        if (total_sum - d) < 0 or (total_sum-d) % 2 == 1 :
            return 0
        
        target = (total_sum - d) // 2
        
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        
        # all subsets can form target 0
        for i in range(n+1):
            dp[i][0] = 1
        
        for i  in range(1,n+1):
            for j in range(target+1):
                include = 0
                if arr[i-1] <= j:
                    include = dp[i-1][j - arr[i-1]]
                exclude = dp[i-1][j]
                
                dp[i][j] = (include + exclude)%MOD
        
        return dp[n][target]
      
