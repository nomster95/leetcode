class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        window_sum = sum(arr[0:k])
        count = 0
        avg = window_sum/k
        if avg>=threshold:
            count+=1
        l,r= 0,k
        while r<len(arr):
            window_sum = window_sum + arr[r]-arr[l]
            max_avg = window_sum/k
            if max_avg>=threshold:
                count+=1
            l+=1
            r+=1

        return count            
            
        