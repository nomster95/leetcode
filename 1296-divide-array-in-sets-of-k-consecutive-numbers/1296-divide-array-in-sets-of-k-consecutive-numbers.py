class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False

        nums.sort()
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in nums:
            if freq[i]==0:
                continue

            need = freq[i]
            for x in range(i,i+k):
                if freq.get(x,0)<need:
                    return False

                freq[x]-=need

        return True        



        
                    



        