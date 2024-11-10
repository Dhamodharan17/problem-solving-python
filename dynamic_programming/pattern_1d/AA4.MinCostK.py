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

#Bottom UP
class Solution:
    def minimizeCost(self, k, arr):
        
        length = len(arr)
        dp = [float('inf')] * length
        dp[0] = 0 # energy req. to reach 0
        
        for n in range(1,length):
            globalMincost = float('inf')
            # Find min cost jump at current n
            for i in range(1,k+1):
                jump = n-i
                if jump >= 0:
                   current_jump = abs(arr[n] - arr[jump])
                   #Take remaining from dp array
                   #In top down , we call function for remaning
                   globalMincost = min(globalMincost,current_jump + dp[jump] )
            dp[n] = globalMincost
            
        return  dp[length-1]
            
