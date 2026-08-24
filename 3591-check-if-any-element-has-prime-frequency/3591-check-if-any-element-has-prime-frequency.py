class Solution:
    def prime(self,n):
        if n<2:
            return False 
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False

        return True        
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1

        for i in freq:
            if self.prime(freq[i]) == True:
                return True

        return False        
            




        