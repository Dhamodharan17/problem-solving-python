class Solution:
    def LongestBitonicSequence(self, n: int, nums: List[int]) -> int:
        dp_fw = [1] * n  # Forward DP for LIS
        dp_bw = [1] * n  # Backward DP for LDS

        # Calculate LIS for forward direction
        for cur in range(n):
            for prev in range(cur):
                if nums[prev] < nums[cur] and dp_fw[cur] < dp_fw[prev] + 1:
                    dp_fw[cur] = dp_fw[prev] + 1

        # Calculate LDS for backward direction
        for cur in range(n - 1, -1, -1):
            for next in range(cur + 1, n):
                if nums[next] < nums[cur] and dp_bw[cur] < dp_bw[next] + 1:
                    dp_bw[cur] = dp_bw[next] + 1

        # Find the maximum bitonic subsequence length
        maxi = 0
        for i in range(n):
            # Subtract 1 because the current element is counted twice
            maxi = max(maxi, dp_fw[i] + dp_bw[i] - 1)

        return maxi
