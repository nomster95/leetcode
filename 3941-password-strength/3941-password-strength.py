class Solution:
    def passwordStrength(self, password: str) -> int:
        ans = 0
        for i in set(password):
            if i.isdigit():
                ans+=3
            elif i.isupper():
                ans+=2 
            elif i.islower():
                ans+=1
            else:
                ans+=5

        return ans                   
        