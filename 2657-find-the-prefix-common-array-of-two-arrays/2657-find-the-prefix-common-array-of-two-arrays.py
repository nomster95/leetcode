class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            freq = {}
            ops = 0
            for j in range(i+1):
                if A[j] not in freq:
                    freq[A[j]]=1
                else:
                    freq[A[j]]+=1

                if B[j] not in freq:
                    freq[B[j]] = 1
                else:
                    freq[B[j]]+=1

            for i in freq:
                if freq[i]==2:
                    ops+=1

            ans.append(ops)   

        return ans    
                    
                    


        