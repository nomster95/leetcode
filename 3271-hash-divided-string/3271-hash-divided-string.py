class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []
        for i in range(0,len(s),k):
            chunk = s[i:i+k]
            ans = 0

            for ch in chunk:
                ans+= ord(ch)-ord('a')
                hashedChar = ans%26
            result.append(chr(ord('a')+hashedChar))

        return "".join(result)    
