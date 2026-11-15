class Solution:
    def kadane(self,nums):
        n = len(nums)
        curr_sum = 0
        max_sum = nums[0]
        for i in range(n):
            curr_sum+=nums[i]

            if curr_sum>max_sum:
                max_sum = curr_sum

            if curr_sum<0:
                curr_sum = 0

        return max_sum        

    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        profit1 = [0]*n
        profit2 = [0]*n
        for i in range(n):
            profit1[i] = nums2[i]-nums1[i]
            profit2[i] = nums1[i]-nums2[i]

        ans1 = self.kadane(profit1)
        ans2 = self.kadane(profit2)

        return max(ans1+sum(nums1),ans2+sum(nums2))    

            

       
        
        return max_sum            


        