class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        ans = []
        n = len(s)
        if len(s)==1:
            return s
            
        if k==1:
            for _ in range(n-1):
                new_s = s[k:] + s[:k]
                s = new_s
                ans.append(s)


            return sorted(ans)[0]  




            

        else:
            return ''.join(sorted(s))


        