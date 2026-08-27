class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for i in range(len(queries)):
            idx = queries[i][0]
            while idx<=queries[i][1]:
                nums[idx] = (nums[idx]*queries[i][3])%((10**9)+7)
                idx+=queries[i][2]

        XOR = 0
        for i in nums:
            XOR = XOR^i

        return XOR    
        