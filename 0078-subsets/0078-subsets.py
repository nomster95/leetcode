class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = 1<<n
        ans = []
        for num in range(subsets):
            store = []
            for i in range(n):
                if num&(1<<i)!=0:
                    store.append(nums[i])

            ans.append(store)  

        return ans          


    