class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        n = len(s)
        count = left = right = 0
        cur_set = Counter()
        while right < n:

            cur_set[s[right]] += 1

            if right - left == 2:
                
                if len(cur_set) == 3:
                    count += 1

                cur_set[s[left]] -= 1
                if cur_set[s[left]] == 0:
                    del cur_set[s[left]]
                left += 1

            right += 1
        
        return count



    

        # for i in range(n-2):
        #     cur_set = set(s[i:i+3])
        #     if len(cur_set) == 3:
        #         count += 1
        
        return count
        
