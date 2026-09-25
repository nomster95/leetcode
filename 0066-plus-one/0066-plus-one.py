class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num+=str(i)

        ans = int(num)+1

        plus_one = []
        for j in str(ans):
            plus_one.append(int(j))

        return plus_one        
        

        