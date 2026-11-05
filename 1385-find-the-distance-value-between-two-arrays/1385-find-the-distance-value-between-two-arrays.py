class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        n  = len(arr1)
        m = len(arr2)
        for i in range(n):
            dist = True
            for j in range(m):
                if abs(arr1[i]-arr2[j])<=d:
                    dist = False

            if dist:
                ans+=1        


        return ans            

        
        
        