class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        seen = set()
        st = []
        for x in s:
            freq[x]-=1
            if x not in seen:
                while len(st)!=0 and st[-1]>x and freq[st[-1]]>0:
                    pc = st.pop()
                    seen.remove(pc)

                st.append(x)
                seen.add(x)

        return "".join(st)                    

        