class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n, ans = len(nums),float('-inf')

        left = right = total = 0
        while right < n:
            total += nums[right]
          #reached window
            if right - left == k-1:
                ans = max(ans, total/k)
                total -= nums[left] #reduce effect
                left+=1
            
            right += 1
        
        return ans
            
        # #generate k subarray
        # for i in range(n-k+1):
        #     total = 0
        #     for j in range(i, i+k):
        #         total += nums[j]
        #     ans = max(ans, total/k)
        
        # return ans
                
