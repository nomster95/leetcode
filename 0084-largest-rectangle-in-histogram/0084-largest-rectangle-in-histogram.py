class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        st = []
        maxArea = 0
        for i in range(len(heights)):
            while len(st)!=0 and heights[st[-1]]>=heights[i]:
                element = st[-1]
                st.pop()
                nse = i
                if len(st)==0:
                    pse = -1
                else:
                    pse = st[-1]

                maxArea = max(maxArea,heights[element]*(nse-pse-1))    

            st.append(i)

        while len(st)!=0:
            nse = len(heights)
            element = st[-1]
            st.pop()
            if len(st)==0:
                pse = -1
            else:
                pse = st[-1]

            maxArea = max(maxArea,heights[element]*(nse-pse-1))  

        return maxArea        



        