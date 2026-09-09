class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        positive = []
        index = []
        for i in range(len(nums)):
            if nums[i]>=0:
                positive.append(nums[i])
                index.append(i)

        if len(positive)>0:
            k = k%len(positive)


        rotated = positive[k:] + positive[:k]  
        for i in range(len(index)):
            nums[index[i]] = rotated[i]

        return nums             