class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans , sol = [] , []
        def backtrack(start):
            if len(sol)==4:
                if start==len(s):
                    ans.append(".".join(sol))
                return

            for end in range(start,min(start+3,len(s))):
                part = s[start:end+1]

                if int(part)>255:
                    continue

                if len(part)>1 and part[0]=="0":
                    continue    

                sol.append(part)
                backtrack(end+1)
                sol.pop()

        backtrack(0)
        return ans                


        