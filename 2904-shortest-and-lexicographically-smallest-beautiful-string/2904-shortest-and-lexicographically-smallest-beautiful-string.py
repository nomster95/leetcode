class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        min_len = float('inf')
        ans = []

        for i in range(len(s)):
            for j in range(i,len(s)):
                arr = s[i:j+1]
                ones = 0
                for x in arr:
                    if x=="1":
                        ones+=1

                if ones==k:
                    ans.append(arr)

        if len(ans)==0:
            return ""            

        ans.sort()
        ans.sort(key=lambda x: len(x))
        return ans[0]        


        