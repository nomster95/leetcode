import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        res = ""
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        h = []  
        for char, cnt in freq.items():
            heapq.heappush(h, (-cnt, char))

        prev = None
        while h or prev:
            if prev and not h:
                return ""

            cnt,char = heapq.heappop(h)
            res+=char
            cnt+=1

            if prev:
                heapq.heappush(h,prev)
                prev = None
            if cnt!=0:
                prev = (cnt,char)

        return res               



        