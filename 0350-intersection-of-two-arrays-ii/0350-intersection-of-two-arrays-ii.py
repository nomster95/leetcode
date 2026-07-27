class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        lst = []
        for i in nums1:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in nums2:
            if i in freq and freq[i]>0:
                lst.append(i)
                freq[i]-=1
               
        return lst