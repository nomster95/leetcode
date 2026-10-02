class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = [0]*len(s)
        for i in range(len(s)):
            arr[i] = abs(ord(s[i])-ord(t[i]))

        l,r = 0,0
        max_len = 0
        sums = 0
        while r<len(arr):
            sums+=arr[r]

            while sums>maxCost:
                sums-=arr[l]
                l+=1

            max_len = max(max_len,r-l+1)
            r+=1

        return max_len    




        