class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        prefix_xor = [0]*(len(arr)+1)
        for i in range(len(arr)):
            prefix_xor[i+1] = arr[i]^prefix_xor[i]

        ans = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                prefix = prefix_xor[j+1]^prefix_xor[i]

                if prefix==0:
                    ans+=(j-i)

        return ans                


        