class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        valid = 0
        for i in range(len(nums)):
            x = 0
            y = 0
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    x+=1
                else:
                    y+=1

                if y>0 and b*x<=a*y:
                    valid+=1

        return valid            


        