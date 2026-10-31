class Solution:
    def isValid(self, s: str) -> bool:
        st = [] 
        for i in range(len(s)):
            st.append(s[i])
            while len(st)>=3 and st[-3]=="a" and st[-2]=="b" and st[-1]=="c":
                st.pop()
                st.pop()
                st.pop()

        if len(st)==0:
            return True
        else:
            return False            
                
        