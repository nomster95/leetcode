class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        ans = set(nums)
        for i in range(len(moveFrom)):
            ans.remove(moveFrom[i])
            ans.add(moveTo[i])


        lst = list(ans)
        lst.sort()
        return lst    
        
        