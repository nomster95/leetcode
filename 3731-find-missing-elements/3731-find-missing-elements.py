class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        n1 = min(nums)
        n2 = max(nums)
        for i in range(n1+1,n2):
            if i not in nums:
                ans.append(i)

        return ans        
        