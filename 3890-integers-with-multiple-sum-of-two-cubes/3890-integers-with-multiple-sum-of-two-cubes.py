class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        freq = {}
        ans = []
        limit = int(n**(1/3))+1
        for a in range(limit):
            for b in range(a,limit):
                total = a**3+b**3
                if total>n:
                    break

                if total not in freq:
                    freq[total] = 1
                else:
                    freq[total]+=1

        for i in freq:
            if freq[i]>=2:
                ans.append(i)

        ans.sort()        

        return ans                    



        