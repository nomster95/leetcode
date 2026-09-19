class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        XOR_prefix = [0]*(len(arr)+1)
        ans = [0]*len(queries)
        for i in range(len(arr)):
            XOR_prefix[i+1] = XOR_prefix[i]^arr[i]

        for i in range(len(queries)):
            ans[i] = XOR_prefix[(queries[i][1])+1]^XOR_prefix[queries[i][0]]


        return ans    


        
        