class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        arr = [0]*len(perm)
        original  = perm.copy()
        count = 0


        while True:
            for i in range(n):
                if i%2==0:
                    arr[i] = perm[i//2]
                else:
                    arr[i] = perm[(n//2) + ((i-1)//2)] 

            count+=1
            perm = arr.copy()
            if perm == original:
                break

        return count                  

            
            