
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ans = []
        for i in nums:
            ans.append(int(i))

        ans.sort()
        return str(ans[-k])    

        