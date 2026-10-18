class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        diff = []
        ans = 0
        for i in range(len(rocks)):
            diff.append(capacity[i]-rocks[i])

        diff.sort()
        for i in range(len(diff)):
            if additionalRocks>=diff[i]:
                additionalRocks-=diff[i]
                ans+=1
            else:
                break

        return ans            
            


        