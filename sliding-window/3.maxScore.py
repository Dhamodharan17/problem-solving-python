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

        
