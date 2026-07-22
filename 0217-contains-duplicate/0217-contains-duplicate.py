class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for i in nums:
            if(i not in store):
                store.add(i)
            else:
                return True

        return False            
        