class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        steps = 0
        rem = capacity
        for i in range(len(plants)):

           
            if rem>=plants[i]:
                steps+=1
                rem-=plants[i] 
            elif rem<plants[i]:
                steps+=(2*i)+1
                rem = capacity-plants[i]


        return steps       


        