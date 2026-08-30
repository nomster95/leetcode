class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums),3):
            part = nums[i:i+3]
            for j in range(len(part)-1):
                if part[j+1]-part[j]>k or part[-1]-part[0]>k:
                    return []

            ans.append(part)

        return ans    

         


        

        