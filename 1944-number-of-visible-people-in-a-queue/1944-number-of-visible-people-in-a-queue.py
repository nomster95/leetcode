class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        st = []
        ans = [0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            count = 0
            while len(st)!=0 and heights[i]>=st[-1]:
                st.pop()
                count+=1

            if len(st)!=0:
                count+=1

            ans[i] = count    
            st.append(heights[i])      

        return ans      



        