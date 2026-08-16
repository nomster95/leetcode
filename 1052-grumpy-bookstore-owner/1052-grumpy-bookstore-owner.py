class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        for i in range(len(customers)):
            if grumpy[i]==0:
                satisfied = satisfied + customers[i]

        saved = sum(customers[0:minutes])
        for i in range(minutes):
            if grumpy[i]==0:
                saved  = saved - customers[i]
        max_saved = saved         
        l,r = 0,minutes
        while r<len(customers):
            if grumpy[r]==1:
                saved = saved + customers[r]

            if grumpy[l]==1:
                saved = saved - customers[l]    


            max_saved = max(max_saved,saved) 
            l+=1
            r+=1

        return max_saved+satisfied     


        