class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        
       
        
        numss = set(nums)
        for i in numss:
            if i-1 not in numss:
                l = 1
                current = i
                while current+1 in numss:
                    current+=1
                    l+=1
                answer = max(answer,l) 

        return answer           
