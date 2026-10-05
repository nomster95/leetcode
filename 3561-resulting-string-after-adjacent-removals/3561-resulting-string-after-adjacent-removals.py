class Solution:
    def resultingString(self, s: str) -> str:
        if len(s)==1:
            return s
        st = []
        for i in s:
            st.append(i)
            while len(st)>=2 and (abs(ord(st[-1])-ord(st[-2]))==1 or abs(ord(st[-1])-ord(st[-2]))==25):
                st.pop()
                st.pop()

            

        return "".join(st)        