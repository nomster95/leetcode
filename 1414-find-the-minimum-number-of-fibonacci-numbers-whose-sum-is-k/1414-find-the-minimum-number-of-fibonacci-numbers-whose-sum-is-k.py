class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k<=2:
            return 1

        seq = [1,1]
        i,j = 0,1
        while seq[i]+seq[j]<=k:  
            seq.append(seq[i]+seq[j])
            i+=1
            j+=1

        ops = 0
        x = len(seq)-1    

        while k!=0:
            if seq[x]<=k:
                k-=seq[x]
                ops+=1

            x-=1

        return ops        
            





        