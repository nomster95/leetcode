class Solution:
    def splitArray(self, nums: List[int]) -> int:
        A = []
        B = []
        for i in range(len(nums)):
            is_prime = True
            if i<2:
                is_prime = False
            for j in range(2,int(sqrt(i))+1):
                if i%j==0:
                    is_prime = False
                    break

            if is_prime:
                A.append(nums[i])
            else:
                B.append(nums[i])

        return abs(sum(A)-sum(B))                    



        