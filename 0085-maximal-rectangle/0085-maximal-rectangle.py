class Solution:
    def area(self,heights):
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

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        max_ones_Area = 0
        prefix = [[0]*m for _ in range(n)]
        for j in range(m):
            sums = 0
            for i in range(n):
                sums+=int(matrix[i][j])
                if matrix[i][j]=="0":
                    sums = 0

                prefix[i][j] = sums

        for k in range(n):
            max_ones_Area = max(max_ones_Area,self.area(prefix[k]))  

        return max_ones_Area             
        