class Solution:
    def next_smaller(self,arr1):
        n = len(arr1)
        st = []
        nse = [-1]*n
        for i in range(n-1,-1,-1):
            while len(st)!=0 and arr1[st[-1]]>=arr1[i]:
                st.pop()

            if len(st)==0:
                nse[i] = n
            else:
                nse[i] = st[-1]

            st.append(i)    

        return nse

    def previous_smaller(self,arr2):
        n = len(arr2)   
        st =[]
        psee = [-1]*n
        for i in range(n):
            while len(st)!=0 and arr2[st[-1]]>arr2[i]:
                st.pop()

            if len(st)==0:
                psee[i] = -1
            else:
                psee[i] = st[-1]

            st.append(i)    

        return psee                         

    def sumSubarrayMins(self, arr: List[int]) -> int:
        total = 0
        nse = self.next_smaller(arr)
        psee = self.previous_smaller(arr)
        mod = 10**9 + 7
        for i in range(len(arr)):
            left = i - psee[i]
            right = nse[i] - i
            total = (total + ((left*right)*arr[i]))%mod

        return total    
        