class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        store = set(nums)
        curr = k
        while curr in store:
            curr+=k

        return curr    


        
        