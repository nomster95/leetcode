class Solution:
    def reverseParentheses(self, s: str) -> str:   
        st = []
        for i in range(len(s)):  
            if s[i]=="(":
                st.append(s[i])
            elif s[i]==")":
                key = ""
                while st[-1]!="(" and len(st)!=0:
                    ans = st.pop()
                    key+=ans

                st.pop()
                for j in key:
                    st.append(j)

            if s[i]!=")" and s[i]!="(":        
                st.append(s[i])


        return "".join(st)    






                    
            

