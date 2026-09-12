class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []
        for x in s:
            st.append(x) 
            if len(st)>=len(part):
                if ''.join(st[-len(part):])==part:
                    for i in range(len(part)):
                        st.pop()

              
                

        return "".join(st)            

        