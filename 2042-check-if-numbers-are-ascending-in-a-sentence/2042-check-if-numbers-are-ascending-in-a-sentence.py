class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lst = s.split()
        ans = []
        for i in lst:
            if i.isdigit():
                ans.append(int(i))

        for i in range(len(ans)-1):
            if ans[i]>=ans[i+1]:
                return False

        return True                
        