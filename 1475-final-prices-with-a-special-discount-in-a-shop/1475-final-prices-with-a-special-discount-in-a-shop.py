class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        n = len(prices)
        discounts = [0]*n
        for i in range(n-1,-1,-1):
            while len(st)!=0 and st[-1]>prices[i]:
                st.pop()

            if len(st)==0:
                discounts[i] = prices[i]
            else:
                discounts[i] = prices[i] - st[-1]

            st.append(prices[i]) 

        return discounts               

        