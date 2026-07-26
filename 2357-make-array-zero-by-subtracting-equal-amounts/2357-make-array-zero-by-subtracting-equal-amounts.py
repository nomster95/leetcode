class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a = set()
        for i in nums:
            if i!= 0:
                a.add(i)

        return len(a)        

        