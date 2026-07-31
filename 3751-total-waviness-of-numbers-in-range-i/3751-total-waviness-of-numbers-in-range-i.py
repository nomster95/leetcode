class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for i in range(num1,num2+1):
            num = str(i)
            n = len(num)
            for j in range(1,n-1):


                if int(num[j])>int(num[j-1]) and int(num[j])>int(num[j+1]):

                    waviness+=1
                elif int(num[j])<int(num[j-1]) and int(num[j])<int(num[j+1]):
                    waviness+=1

                
        return waviness        
                       


        