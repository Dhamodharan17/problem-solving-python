#recursion
class Solution:
	def perfectSum(self, arr, n, sum):
		
		def util(i, target):
		    #smallest problem - when sum = 0 any set can make it by empty set
		    if target == 0 :
		        return 1
		    
		    if i < 0 :
		        return 0
		    
		    pick = 0
		    if arr[i] <= target :
		        pick = util(i-1, target - arr[i])
            
            skip = util(i-1, target)
            
            return pick + skip
        
        return util(n-1, sum)

#bottom up
class Solution:
	def perfectSum(self, arr, n, sum):
	   MOD = 10**9 + 7  # Modulo value
	   dp = [[0 for _ in range(sum+1)] for _ in range(n+1)]
	    
	   # all subsets can make sum 0
	   for i in range(n+1):
	        dp[i][0] = 1
	   
	   for i in range(1,n+1):
	       # start from sum 0, since sum element can be 0
	       for cur_sum in range(0,sum+1):
	            pick = 0
	            if arr[i-1] <= cur_sum:
	                pick = dp[i-1][cur_sum - arr[i-1]] % MOD
	            skip = dp[i-1][cur_sum] % MOD
	            dp[i][cur_sum] = (pick + skip) % MOD
	            
	   return dp[n][sum]

#space
class Solution:
	def perfectSum(self, arr, n, sum):
	    
	   MOD = 10**9 + 7 
	   
	   prev = [0 for _ in range(sum+1)]
	   # since all subsets can make 0
	   prev[0] = 1
	   
	   for i in range(1,n+1):
	       current = [0 for _ in range(sum+1)]
	       current[0] = 1
	       for cur_sum in range(0,sum+1):
	            pick = 0
	            if arr[i-1] <= cur_sum:
	                pick = prev[cur_sum - arr[i-1]] % MOD
	            skip = prev[cur_sum] % MOD
	            current[cur_sum] = (pick + skip) % MOD
	       prev = current
	   return prev[sum]
