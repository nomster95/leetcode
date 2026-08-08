class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans1 = []
        ans2 = []
        ans = []
        for i in nums:
            if i>0:
                ans1.append(i)
            else:  
                ans2.append(i)  
        
        i,j = 0,0
        while(j<len(ans2)):
            ans.append(ans1[i])
            i+=1
            ans.append(ans2[j])
            j+=1

        return ans    
            