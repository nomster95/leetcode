class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        ans = [0]*k
        freq = {}
        for x,y in logs:
            if x not in freq:
                freq[x] = []
            freq[x].append(y)

        for i in freq:
            ans[len(set(freq[i]))-1]+=1


        return ans         
        