class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        sum = ans = left = right = 0
        index_dict = defaultdict(int)

        while right < n:

            current = nums[right]
            sum += current
            index_dict[current] += 1

            #handle duplicate
            while (index_dict[current] > 1 or right - left == k ) and left < right:
                index_dict[nums[left]] -= 1 #will impact the current count in map
                sum -= nums[left]
                left+=1

            #k window size
            if right - left == k-1:
                ans = max(ans, sum)
                # index_dict[nums[left]] -= 1
                # sum -= nums[left]
                # left += 1
                

            right += 1
        return ans


        #AP1: bruteforce
        # for i in range(n-k+1):
        #     sum = 0
        #     num_set = set()
        #     for j in range(i, i+k):
        #         if nums[j] in num_set:
        #             sum = 0
        #             break
        #         else:
        #              num_set.add(nums[j])
        #              sum = sum + nums[j]
        #     ans = max(ans, sum)
        
        #return ans

def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        sum = ans = left = right = 0
        dupChecker = 0

        while right < n:

            current = nums[right]
            sum += current

            #remove duplicate duplicate
            while ((dupChecker & 1<<current )> 0  or right - left == k ) and left < right:
                dupChecker &= ~ (1 << nums[left]) #unset
                sum -= nums[left]
                left+=1
            
            dupChecker |= (1<<current)  #set

            #k window size
            if right - left == k-1:
                ans = max(ans, sum)                

            right += 1
        return ans

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        sum = ans = left = right = 0
        dup_set = set()

        while right < n:
            current = nums[right]

            if current not in dup_set:
                sum += current
                dup_set.add(current)

                # no duplicate + window size k -> can be answer
                if right - left == k-1:
                    ans = max(ans, sum)

                    #reached window size
                    sum -= nums[left]
                    dup_set.remove(nums[left])
                    left += 1

            else: #duplicate
                # stop when we found the duplicate
                while nums[left] != nums[right]:
                    sum -= nums[left]
                    dup_set.remove(nums[left])
                    left+=1
                #by pass duplicate
                left+=1
            
            right += 1
        
        return ans

