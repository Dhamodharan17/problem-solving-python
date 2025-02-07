class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        result = []
        # we can get min/max easily with monotonic stack/queue
        dq = collections.deque()

        left = right = 0

        while right < n:
            
            # when our window size
            if dq and right - left == k-1:
                result.append(nums[dq[0]])
                dq.popleft() # remove 1st 
                left += 1
            
            # we want greater, if top is less remove it
            #decreasing stack
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop() # remove last
            
            dq.append(right)
            right += 1

        return result



        #AP 1
        # for i in range(n-k+1):
        #     sorted_list = sorted(nums[i:i+k])
        #     result.append(sorted_list[k-1])
        
        # return result
        
