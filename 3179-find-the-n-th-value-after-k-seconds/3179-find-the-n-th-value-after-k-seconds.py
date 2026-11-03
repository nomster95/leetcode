class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        a = [1]*n
        while k!=0:
            
            for i in range(1,n):
                a[i] = a[i] + a[i-1]

            k-=1

        ans = a[-1]%((10**9)+7)   
        return ans     


        