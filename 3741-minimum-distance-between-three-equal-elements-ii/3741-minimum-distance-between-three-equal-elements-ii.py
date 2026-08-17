class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = {}
        ans = float('inf')
        for i, x in enumerate(nums):

            if x not in freq:
                freq[x] = []
            freq[x].append(i)
         
        for i in freq.values():
            distance = 0
            if len(i)>=3:
                for j in range(len(i)-2):
                    distance = 2*(i[j+2]-i[j])
                    ans = min(ans,distance)  

        if ans==float('inf'):
            return -1          


        return ans        
                    


