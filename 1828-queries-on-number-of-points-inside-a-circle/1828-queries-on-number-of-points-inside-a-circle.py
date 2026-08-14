class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        radius = 0
        cx = 0
        cy = 0

        ans = []
        
        for i in queries:
            for j in i:
                radius = i[2]
                cx = i[0]
                cy = i[1]

            count = 0
            for x,y in points:
                dist = ((cx-x)**2 + (cy-y)**2)
                if dist<=radius**2:
                    count+=1

            ans.append(count) 

        return ans           
                   