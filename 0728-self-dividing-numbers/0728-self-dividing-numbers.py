class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            self_deviding = True
            m = i
            while m!=0:
                digit = m%10
                if digit==0:
                    self_deviding = False
                
                if digit!=0 and i%digit!=0:
                    self_deviding = False

                m = m//10    

            if self_deviding:
                ans.append(i)  

        return ans              


        