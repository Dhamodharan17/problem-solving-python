#Recursion
class Solution:
    def minimizeCost(self, k, arr):
        
        n = len(arr)-1
        
        def minimizeUtil(arr, k, n):
            
            if n < 0:
                return float('inf')
            if n == 0:
                return 0
                
            globalMincost = float('inf')
            for i in range(1,k+1):
                jump = n-i
                if jump >= 0:
                   globalMincost = min(globalMincost, abs(arr[n] - arr[jump]) +minimizeUtil(arr, k , jump))
            return globalMincost
            
        return minimizeUtil(arr, k, n)

  #Topdown
  class Solution:
    def minimizeCost(self, k, arr):
        
        n = len(arr)
        dp = [-1] * n
        def minimizeUtil(arr, k, n, dp):
            
            if n < 0:
                return float('inf')
            if n == 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
                
                
            globalMincost = float('inf')
            for i in range(1,k+1):
                jump = n-i
                if jump >= 0:
                   globalMincost = min(globalMincost, abs(arr[n] - arr[jump]) +minimizeUtil(arr, k , jump,dp))
            dp[n] = globalMincost
            return  dp[n]
            
        return minimizeUtil(arr, k, n-1, dp)
