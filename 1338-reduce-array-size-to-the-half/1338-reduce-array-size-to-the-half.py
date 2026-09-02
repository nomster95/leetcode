class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = set()
        freq = {}
        
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        sorts = sorted(freq.items() , key = lambda x: x[1], reverse = True)
        count = 0
        for i in sorts:
            if count>=n//2:
                break
    
            ans.add(i[0])
            count+=i[1]
            

        return len(ans)        
            




        