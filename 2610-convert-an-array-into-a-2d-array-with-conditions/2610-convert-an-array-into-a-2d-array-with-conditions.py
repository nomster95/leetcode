class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x]+=1

        max_freq = max(freq.values())
        ans = [[] for _ in range(max_freq)]

        for value,count in freq.items():
            for row in range(count):
                ans[row].append(value)

        return ans        









                


        

        