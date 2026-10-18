class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        rem_k = k
        rem_n = n
        string = []
        while rem_k>26+(rem_n-1):
            string.append('z')
            rem_k-=26
            rem_n-=1


        rem_char = chr(96+rem_k-(rem_n-1))
        string.append(rem_char)   
        string.reverse()
        suffix = "".join(string)
        return 'a'*(n-len(string))+suffix

        
        