class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        n = len(cards)
        ans = float('inf')

        left = right = 0
        counter = Counter()
        while right < n:

            counter[cards[right]] += 1

            #reduce until current 2 cards go
            while counter[cards[right]] == 2:
                #untill above conditon true , i can have valid picks
                ans = min(ans, right - left + 1)
                counter[cards[left]] -= 1
                left += 1

            right += 1

        return ans if ans != float('inf') else -1




        # AP1 -  bottle neck - finding the count from start all the time
        #once we have required count, we can try some other array
        #since going forward will give more pickups
        # for i in range(n): #start from any card:
        #     counter = Counter()
        #     for j in range(i,n): #pick one by one
        #         counter[cards[j]] += 1

        #         if counter[cards[j]] == 2:
        #             ans = min(ans, j - i+1)
        #             break
        
        # return ans if ans != float('inf') else -1

        
