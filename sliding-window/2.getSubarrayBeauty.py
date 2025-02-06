class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        
        n = len(nums)
        result = [0] * (n-k+1)
        #counting sort
        count = [0] * 101 # -50 to 50

        left = right = neg = p1 = 0

        while right < n:

            if(nums[right]) < 0 : neg+=1
            #offset count increase
            count[nums[right] + 50] +=1

            #c1
            if right - left == k-1:
                #c2
                xthSmallest = self.getXthSmallest(count, x)
                if neg >= x:
                    result[p1] = xthSmallest
                else:
                    result[p1] = 0
                p1+=1

                if(nums[left]) < 0 : neg-=1
                #offset count increase
                count[nums[left] + 50] -=1
                left += 1
            
            right += 1
        
        return result
    
    def getXthSmallest(self,count, x):

        sum = 0
        for i in range(len(count)):
            sum += count[i]
            #since all are counts of elements
            #we want the xth smallest
            if sum >= x:
                return i - 50
        return 0

        # s1 = sortedcontainers.SortedList()

        # while right < n:

        #     s1.add(nums[right])
        #     #c1 - k size array
        #     if right - left == k - 1:
                
        #         #c2 - kth smallest
        #         if s1[x-1] < 0:
        #             result.append(s1[x-1])
        #         else:
        #             result.append(0)

        #         s1.remove(nums[left])
        #         left += 1

        #     right += 1
        
        # return result

        # #c1 -> k size array
        # for i in range(n-k+1):
        #     cur_arr = nums[i:i+k]

        #     #c2 -> xth smallest
        #     cur_arr.sort()
        #     xthElement = cur_arr[x-1]

        #     if xthElement < 0:
        #         result.append(xthElement)
        #     else:
        #         result.append(0)
        
        # return result
            
            
