class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        seen = set()
        for i in s:
            if i not in seen:
                seen.add(i)
            else:
                count+=1
                seen = set()
                seen.add(i)

        return count            


        