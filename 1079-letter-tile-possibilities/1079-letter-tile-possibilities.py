class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = {}
        for i in tiles:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        def backtrack():
            count = 0
            for x in freq:
                if freq[x]>0:
                    count+=1
                    freq[x]-=1

                    count+= backtrack()
                    freq[x]+=1

            return count        

                  

        return backtrack()               


        