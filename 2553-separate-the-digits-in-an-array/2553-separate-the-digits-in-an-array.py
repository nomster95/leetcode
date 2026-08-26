class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            st = str(i)
            for j in st:
                ans.append(int(j))

        return ans        
        