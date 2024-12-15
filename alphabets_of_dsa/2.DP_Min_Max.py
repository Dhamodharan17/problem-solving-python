#top down
class Solution:
    def minimizeCost(self, k, arr):
        
        n = len(arr) - 1
        
        def dp_util(current_index):
            
            # cost to reach 0 from 0
            if current_index == 0:
                return 0
            
            cost = float('inf')
            #k jumps 
            for i in range(1, k+1):
                
                #jump back
                jump_index = current_index-i
                
                if jump_index >= 0:
                # i cannot solve complete -> balance handover to subproblem
                    current_cost = abs(arr[current_index] - arr[jump_index])
                    
                    #subproblem
                    remaining_cost = dp_util(jump_index)
                    
                    cost = min(cost, current_cost + remaining_cost)
                    
            return cost
                    
        return dp_util(n)            
                    
