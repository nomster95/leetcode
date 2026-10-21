class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        indice_arr = sorted(range(n) , key=lambda i: (arr[i],i))
        rank = [0]*n
        for i in range(n):
            rank[indice_arr[i]] = i

        
        running_sum = [0]*len(arr)
        running_sum[0] = rank[0]
        ans = 0
        for i in range(1,len(rank)):
            running_sum[i] = running_sum[i-1] + rank[i]

        for i in range(len(arr)):
            if (i*(i+1))//2==running_sum[i]:
                ans+=1

        return ans            
        