class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = []
        beams = 0
        for i in range(len(bank)):
            ones = 0
            for j in bank[i]:
                if j=="1":
                    ones+=1

            if ones>0:
                ans.append(ones)    


        if len(ans)<=1:
            return 0

        for i in range(len(ans)-1):
            beams+= ans[i]*ans[i+1]
            
        return beams            

        