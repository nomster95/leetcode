class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        n = len(l)
        for i in range(n):
            query = nums[l[i]:r[i]+1]
            query.sort()
            sequence = True
            for j in range(len(query)-2):
                if abs(query[j+1] - query[j])!=abs(query[j+2]-query[j+1]):
                    sequence = False
                
            if sequence:
                ans.append(True)    
            else:
                ans.append(False)        
                    
        return ans            



                

        