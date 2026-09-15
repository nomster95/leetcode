class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        res = 0
        seen = set()
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1

        ans = dict(sorted(freq.items(), key = lambda x:x[1],reverse = True))
        for i in ans:
            while ans[i]>0 and ans[i] in seen:
                ans[i]-=1
                res+=1

            seen.add(ans[i]) 


        return res    

                
                    
        