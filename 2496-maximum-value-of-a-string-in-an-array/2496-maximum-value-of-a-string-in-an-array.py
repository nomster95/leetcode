class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = []
        for i in strs:
            is_digit = True
            for j in i:
                if j.isalpha():
                    is_digit = False

            if is_digit:
                ans.append(int(i))
            else:
                ans.append(len(i))

        return max(ans)                    
