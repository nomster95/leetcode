class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        dig = "123456789"
        ans = []
        min_len = len(str(low))
        max_len = len(str(high))
        for length in range(min_len,max_len+1):
            for i in range(len(dig)-length+1):
                x = int(dig[i:i+length])
                if low<=x<=high:
                    ans.append(x)

        ans.sort()
        return ans            

                

                
            



        