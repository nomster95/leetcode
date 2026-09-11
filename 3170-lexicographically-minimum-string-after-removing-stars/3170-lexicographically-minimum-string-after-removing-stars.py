import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        h = []
        ans = ""
        removed = set()
        for i in range(len(s)):
            if s[i]=="*":
                char,index = heapq.heappop(h)
                removed.add(-index)
            else:   
                heapq.heappush(h,(s[i],-i)) 

        for i in range(len(s)):
            if i not in removed and s[i]!="*":
                ans+=s[i]

        return ans        


                

