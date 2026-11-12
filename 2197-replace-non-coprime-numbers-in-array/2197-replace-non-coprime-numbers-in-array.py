class Solution:
    def hcf(self,a,b):
        while b:
            a,b = b,a%b

        return a

    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        st = []
        for i in nums:
            st.append(i)
            while len(st)>=2 and self.hcf(st[-1],st[-2])>1:
                    lcm = (st[-1]*st[-2])//self.hcf(st[-1],st[-2])
                    st.pop()
                    st.pop()
                    st.append(lcm)

        return st            
                

        