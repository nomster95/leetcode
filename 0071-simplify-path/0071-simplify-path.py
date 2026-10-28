class Solution:
    def simplifyPath(self, path: str) -> str:
        component = path.split("/")
        st = []

        for x in component:
            if x=="..":
                if len(st)!=0:
                    st.pop()
            elif x not in ['','.']:
                st.append(x)

        return '/'+'/'.join(st)                

                
        