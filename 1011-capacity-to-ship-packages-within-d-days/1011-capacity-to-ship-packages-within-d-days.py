class Solution:
    def capacity(self,weights,cap):
        day = 1
        load = 0
        for i in range(len(weights)):
            if load + weights[i]>cap:
                day = day+1
                load = weights[i]
            else:
                load+=weights[i]

        return day        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low<=high:
            mid = (low+high)//2
            no_of_days = self.capacity(weights,mid)
            if no_of_days<=days:
                high = mid-1
            else:
                low = mid+1

        return low            
        


        