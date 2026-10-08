class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        freq1 = {}
        freq2 = {}
        ans = 0
        for i in nums1:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i]+=1

        for j in nums2:
            if j not in freq2:
                freq2[j] = 1
            else:
                freq2[j]+=1                

        for x in set(nums1) | set(nums2):
            c1 = freq1.get(x,0)
            c2 = freq2.get(x,0)
            if (c1+c2)%2!=0:
                return -1
            diff = abs(c1-c2)
            ans+=diff


        return ans//4        






        