class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq = {}
        ans = [] 
        for i in words2:
            temp = {}
            for j in i:
                if j not in temp:
                    temp[j] = 1
                else:
                    temp[j]+=1

            for j in temp:
                freq[j] = max(freq.get(j, 0), temp[j])        

        for i in words1:
            freq1 = freq.copy()
            for j in i:
                if j in freq1:
                    freq1[j]-=1

            if all(x <= 0 for x in freq1.values()):
                ans.append(i)

        return ans                
            

            

        