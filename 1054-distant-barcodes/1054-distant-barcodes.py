import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = {}
        res = []
        for i in barcodes:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        h = []  
        for char, cnt in freq.items():
            heapq.heappush(h, (-cnt, char))

        prev = None
        while h or prev:

            cnt,char = heapq.heappop(h)
            res.append(char)
            cnt+=1

            if prev:
                heapq.heappush(h,prev)
                prev = None
            if cnt!=0:
                prev = (cnt,char)

        return res               


        