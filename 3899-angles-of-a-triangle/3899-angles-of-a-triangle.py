import math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        #cosine formula use karna hoga...
        ans = []
        
        
        sides.sort()
        a = sides[0]
        b = sides[1]
        c = sides[2]   
        

        triangle_valid = True
        if a+b<=c:
            triangle_valid = False

        if triangle_valid:
            A  = math.acos((a**2+b**2-c**2)/(2*a*b)) #math.acos for radians
            B  = math.acos((c**2+b**2-a**2)/(2*c*b))
            C  = math.acos((a**2+c**2-b**2)/(2*a*c))

            ans.append(math.degrees(A)) #math.degrees for degree
            ans.append(math.degrees(B))
            ans.append(math.degrees(C))
        else:
            return [] 

        ans.sort()
        return ans        
            



            




        