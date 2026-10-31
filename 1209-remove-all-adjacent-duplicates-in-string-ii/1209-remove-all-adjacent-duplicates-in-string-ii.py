class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        ans = ""
        for i in s:
            if st and st[-1][0]==i:
                st[-1][1]+=1
            else:
                st.append([i,1])

            if st and st[-1][1]==k:
                st.pop()

        for x in st:
            a , b = x
            ans+=a*b

        return ans    



                       
        