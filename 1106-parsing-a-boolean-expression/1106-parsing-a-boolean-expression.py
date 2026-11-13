class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for ch in expression:
            if ch==",":
                continue
            elif ch!=")":
                st.append(ch)
            else:
                vals = []
                while st[-1]!="(":
                    vals.append(st.pop())

                st.pop()
                op = st.pop()
                if op=="!":
                    res = "t" if vals[0]=="f" else "f"

                elif op=="|":
                    res = 't' if any(x=="t" for x in vals) else 'f'

                elif op=="&":
                    res = 't' if all(x=="t" for x in vals) else 'f'

                st.append(res)

        if st[0]=="t":
            return True
        return False                        

                    
                    


    
                                   
        