class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        unique_count = len(set(arr))
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        ans = sorted(freq.items(), key = lambda x: x[1])        
        for i in ans:
            if k>=i[1]:
                k-=i[1]
                unique_count-=1
            else:
                break

        return unique_count            


                