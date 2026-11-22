class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        seen = set()
        for ch in words:
            even = ""
            odd = ""
            for i in range(len(ch)):
                if i%2==0:
                    even+=ch[i]
                else:
                    odd+=ch[i]


            even_s = sorted(even)
            odd_s = sorted(odd)        
            word = "".join(even_s+odd_s)
            if word not in seen:
                seen.add(word)

        return len(seen)         

        