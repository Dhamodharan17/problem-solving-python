class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        ans = 0
        for i in range(k):
            fsum = 0
            for i1 in range(i+1):
                fsum += cardPoints[i1]
            bsum = 0
            # if i == k:
            #     ans = max(ans, fsum)
            #     continue

            for j in range(n-1, n-k+i,-1):
                bsum += cardPoints[j]
            ans = max(ans, fsum+bsum)
        
        #last k elements
        bsum = 0
        for j in range(n-1, n-k-1,-1):
            bsum += cardPoints[j]

        return max(ans, bsum)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        ans, n = 0, len(cardPoints)

        prefix_sum = [0] * n
        prefix_sum[0] = cardPoints[0]
        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + cardPoints[i]

        suffix_sum = [0] * n
        suffix_sum[n-1] = cardPoints[n-1]
        for i in range(n-2,-1,-1):
            suffix_sum[i] = suffix_sum[i+1] + cardPoints[i]

            
        for i in range(k):
            fsum = prefix_sum[i]
            print(i)
            bsum = 0 if i== k-1 else suffix_sum[n-k+i+1]
            print(n-k+i)
            ans = max(ans, fsum+bsum)
        
        ans = max(ans,suffix_sum[n-k])
        return ans

        
