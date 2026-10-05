class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for i in s:
            if i=="(":
                st.append(0)
            else:
                if st[-1]==0:
                    st.pop()
                    st[-1]+=1
                else:
                    x = st.pop()
                    st[-1]+=x*2

        return st[-1]                    
        