class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i in range(len(variables)):
            a = variables[i][0]
            b = variables[i][1]
            c = variables[i][2]
            m = variables[i][3]
            formula = (((a**b)%10)**c)%m 
            if formula==target:
                ans.append(i)

        return ans        

           


        