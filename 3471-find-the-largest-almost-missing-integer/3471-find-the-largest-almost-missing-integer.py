class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = []
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i]==1:
                ans.append(i)

        if k==1:
            if len(ans)==0:
                return -1
            return max(ans)

        if k==n:
            return max(nums)

        if freq[nums[0]]==1 and freq[nums[n-1]]==1:
            return max(nums[0],nums[n-1])
        elif freq[nums[0]]==1 and freq[nums[n-1]]>1:
            return nums[0]
        elif freq[nums[0]]>1 and freq[nums[n-1]]==1:
            return nums[n-1]
        else:
            return -1                






        
        