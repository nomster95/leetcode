class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        leftFreq = {}
        rightFreq = {}
        count = 0
        mod = 10**9 + 7
        for i in nums:
            if i not in rightFreq:
                rightFreq[i] = 1
            else:
                rightFreq[i]+=1

        for j in range(len(nums)):
            rightFreq[nums[j]]-=1
            x = 2*nums[j]
            left = leftFreq.get(x,0)
            right = rightFreq.get(x,0)
            count+=left*right

            leftFreq[nums[j]] = leftFreq.get(nums[j],0)+1


        return count%mod   



        