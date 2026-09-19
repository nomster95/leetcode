class Solution:
    def is_prime(self,n):
        is_prime = True
        if n==1:
            is_prime = False

        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                is_prime = False
                break

        return is_prime            
        

    def completePrime(self, num: int) -> bool:
        if num==1:
            return False

        complete_prime = True 
        s = str(num)  
        for i in range(1,len(s)+1):
            prefix = int(s[:i])
            suffix = int(s[-i:])

            if self.is_prime(prefix)==False:
                return False

            if self.is_prime(suffix)==False:
                return False   


        return True         

            

        





        