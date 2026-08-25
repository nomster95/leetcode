class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        freq = {}
        ans = []
        for i in bulbs:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            if freq[i]%2!=0:
                ans.append(i)

        ans.sort()
        return ans       

        