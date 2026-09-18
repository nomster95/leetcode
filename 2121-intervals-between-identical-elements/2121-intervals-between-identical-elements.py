class Solution:
    def getDistances(self, arr: list[int]) -> list[int]:
        freq = {}
        ans = [0]*len(arr)
        for i,val in enumerate(arr):
            if val not in freq:
                freq[val] = []
            freq[val].append(i)

        for x in freq:
            nums = freq[x]
            prefix = [0]*(len(nums)+1)
            for i in range(len(nums)):
                prefix[i+1] = nums[i] + prefix[i]

            for i in range(len(nums)):
                left = nums[i]*i - prefix[i]
                right_count = len(nums)-i-1
                right_sum = prefix[-1] - prefix[i+1]
                right = right_sum - nums[i]*right_count
                dist = left + right

                ans[nums[i]] = dist

        return ans        



        