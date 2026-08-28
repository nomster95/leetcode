class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,j = 0,0
        st = []
        while i<len(pushed):
            st.append(pushed[i])

            while len(st)!=0 and st[-1]==popped[j]:
                st.pop()
                j+=1

            i+=1    
            
        if len(st)==0:
            return True

        return False                
        




        