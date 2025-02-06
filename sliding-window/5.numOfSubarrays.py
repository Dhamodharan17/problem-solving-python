class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        n , count = len(arr), 0
        left = right = total = 0

        while right < n:
            total += arr[right]

            if right - left == k-1:
                if total // k >= threshold:
                    count += 1
                total -= arr[left]
                left += 1
            right += 1
        
        return count

        #generate k subarray
        # for i in range(n-k+1):
        #     total = 0
        #     for j in range(i, i+k):
        #         total += arr[j]
        #     if total // k >= threshold:
        #         count += 1
        
        # return count
        
