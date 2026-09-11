class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in range(len(num)):
            while len(st)!=0 and k>0 and st[-1]>num[i]:
                st.pop()
                k-=1
            st.append(num[i])

        while k>0:
            st.pop()
            k-=1

        ans = "".join(st).lstrip('0')
        return ans if ans else '0'
        

       

        