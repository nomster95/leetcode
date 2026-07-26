class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = set(nums)
        n = len(nums)
        missing = []
        for i in range(1,n+1):
            if i not in m:
                missing.append(i)

        return missing        


      