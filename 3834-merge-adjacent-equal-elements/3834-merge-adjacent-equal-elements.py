class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            st.append(x)
            while len(st)>=2 and st[-1]==st[-2]:
                x1 = st.pop()
                x2 = st.pop()
                st.append(x1 + x2)


        return st        


        