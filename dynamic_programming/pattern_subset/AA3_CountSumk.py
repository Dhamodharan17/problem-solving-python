#recursion
class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		
		def util(current_index, current_target):
		    
		    if current_target == 0:
		        return 1
	        
	        if current_index < 0:
	            return 0
	        
	        take = 0
	        if arr[current_index] <= current_target:
	            take = util(current_index-1, current_target-arr[current_index])
	       
	        skip = util(current_index-1, current_target)
	       
	        return skip + take
	       
	    return util(n-1, sum)

#topdown
