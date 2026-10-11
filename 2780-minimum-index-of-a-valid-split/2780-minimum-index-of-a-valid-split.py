class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        ans = -1
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

       
        
        max_e = max(freq , key=freq.get)
        max_f = freq[max_e]
        f1 = 0

        for i in range(n-1):
            if nums[i]==max_e:
                f1+=1
            f2 = max_f - f1
            if f1*2>i+1 and f2*2>n-i-1:
                ans = i
                break

        return ans               



                 
        