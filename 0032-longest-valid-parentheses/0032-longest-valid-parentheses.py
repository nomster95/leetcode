class Solution:
    def longestValidParentheses(self, s: str) -> int:
        opens = 0
        closed = 0
        max_len = 0
        start = 0
        for i in range(len(s)):
            if s[i]=="(":
                opens+=1
            else:
                closed+=1

            if closed>opens:
                start = i+1
                opens = 0
                closed = 0

            if opens==closed:
                max_len = max(max_len,i-start+1)

        end = len(s)-1
        opens = 0
        closed = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="(":
                opens+=1
            else:
                closed+=1

            if opens>closed:
                end = i-1
                opens = 0
                closed = 0


            if opens==closed:
                max_len = max(max_len,end-i+1)

        return max_len                            




        