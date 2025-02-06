class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ns = len(s)
        np = len(p)
        p_counter = Counter(p)
        result = []

        s_counter = Counter()
        left = right = 0
        while right < ns:

            s_counter[s[right]] += 1

            if s_counter == p_counter:
                result.append(left)
            
            if right - left == np-1:
                if s_counter[s[left]] - 1 == 0:
                    del s_counter[s[left]]
                else:
                    s_counter[s[left]] -= 1
                left+=1

            right += 1
            
        return result

            


        #generate all string of size p
        #check characters are equal

        # for i in range(ns-np+1):
        #     cur_counter = Counter(s[i:i+np])
        #     if cur_counter == p_counter:
        #         result.append(i)
        
        # return result





        
