class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        freq = {}
        ans = [0]*len(nums)
        for i,val in enumerate(nums):
            if val not in freq:
                freq[val] = []
            freq[val].append(i)

        for x in freq:
            arr = freq[x]
            prefix = [0]*(len(arr)+1)
            for i in range(len(arr)):
                prefix[i+1] = arr[i] + prefix[i]

            for i in range(len(arr)):
                left = arr[i]*i - prefix[i]
                right_count = len(arr)-i-1
                right_sum = prefix[-1] - prefix[i+1]
                right = right_sum - arr[i]*right_count
                dist = left + right

                ans[arr[i]] = dist

        return ans        




        