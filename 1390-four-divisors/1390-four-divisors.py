class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            div_sum = 0
            div = []
            for j in range(1,int(nums[i]**0.5)+1):
                if nums[i]%j==0:
                    div.append(j)
                    if j!=nums[i]//j:
                        div.append(nums[i]//j)

            if len(div)==4:
                div_sum+= sum(div)        


            ans+=div_sum        
        
        return ans