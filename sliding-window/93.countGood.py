class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        n, count = len(nums), 0
        #generate all subarray
        for start in range(n):#index 0 to n - start subbarrays
           
            #generating pairs for subaray 0 to n
            for end in range(start, n):
                # index 0, 1, 2, 3 - intermediate subarray
                subarray = nums[start:end+1]

                local_count = 0
                #generate all pairs from subarray
                for i in range(len(subarray)):# index start to end (smallest subarray)
                    for j in range(i+1,len(subarray)):
                        if subarray[i] == subarray[j]:
                            local_count += 1


                if local_count >= k:
                    count += 1
        return count

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        n, count = len(nums), 0
        left, right = 0, 0
        count_dict = collections.defaultdict(int)

        while right < n :

            count_dict[nums[right]] += 1
            # if same number twice - 1 pair, only once 0 pair
            k -= count_dict[nums[right]]-1

            right += 1
            # shrink since we got enough k's
            while k <= 0:
                #remove pairs
                k += count_dict[nums[left]] - 1;
                count_dict[nums[left]] -= 1
                left += 1
            
            #
            count += left
        
        return count
            
    #✅ The current window [left, right] already has k pairs.
#✅ All subarrays starting from any index ≤ left and ending at right are also valid.
#✅ Instead of checking each subarray manually, we efficiently count them using left.
                




        
        
        
