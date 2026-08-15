class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        count_a = 0
        count_b = 0
        for i in s:
            if i=="a":
                count_a+=1
            if i=="b":
                count_b+=1

        return abs(count_a-count_b)            

        