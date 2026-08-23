class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        nge = []
        freq = {}
        for j in range(len(nums2)-1,-1,-1):

            while len(st)!=0 and st[-1]<nums2[j]:
                st.pop()

            if len(st)==0:
                freq[nums2[j]] = -1
            else:
                freq[nums2[j]] = st[-1]

            st.append(nums2[j])

        for i in nums1:
            if i in freq:
                nge.append(freq[i])

        return nge        



        