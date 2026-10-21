class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        running_sum = [0]*len(arr)
        running_sum[0] = arr[0]
        ans = 0
        for i in range(1,len(arr)):
            running_sum[i] = running_sum[i-1] + arr[i]

        for i in range(len(arr)):
            if (i*(i+1))//2==running_sum[i]:
                ans+=1

        return ans            

          
        