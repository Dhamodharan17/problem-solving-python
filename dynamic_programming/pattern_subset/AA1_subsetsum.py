class Solution:
    #biggger problem - does subset exist in array
    def isSubsetSum (self, arr, target):
        
        n = len(arr)
        
        def util(current_index , target):
            
            if target == 0:
                return True
                
            if current_index < 0 or target < 0:
                return False
            #does subset exist in smaller array of smaller target
            pick = util(current_index-1, target-arr[current_index])
            
            skip = util(current_index-1, target)
            
            return pick or skip
            
        return util(n-1, target)
        
