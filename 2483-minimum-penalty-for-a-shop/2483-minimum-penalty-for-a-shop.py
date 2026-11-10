class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix = [0]*(n+1)
        suffix = [0]*(n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + (customers[i]=="N")

        for j in range(n-1,-1,-1):
            suffix[j] = suffix[j+1] + (customers[j]=="Y")

        penalty = prefix[0] + suffix[0]
        min_index = 0
        for i in range(1,n+1):
            if prefix[i]+suffix[i]<penalty:
                penalty = prefix[i] + suffix[i]
                min_index = i

        return min_index     
        