class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = -1
        distance = 0
        for i in range(len(seats)):
            if seats[i]==1:
                if prev == -1:

                    distance = i-0
                    prev = i
                else:
                    distance = max(distance,(i-prev)//2)
                    prev = i

        return max(distance,len(seats)-1-prev)            



            
            

        





        