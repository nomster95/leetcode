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

        sorted_f = sorted(freq.items() , key=lambda x:x[1] , reverse = True)
        max_e = sorted_f[0][0]
        max_f = sorted_f[0][1]
        f1 = 0

        for i in range(n-1):
            if nums[i]==max_e:
                f1+=1
            f2 = max_f - f1
            if f1*2>i+1 and f2*2>n-i-1:
                ans = i
                break

        return ans               



                 
        