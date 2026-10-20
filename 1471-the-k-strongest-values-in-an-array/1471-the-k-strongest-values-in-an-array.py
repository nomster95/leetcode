class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        median = arr[(len(arr)-1)//2]
        ans = []
        l = 0
        r = len(arr)-1
        while len(ans)!=k:
            if abs(arr[l]-median)>abs(arr[r]-median):
                ans.append(arr[l])
                l+=1
            else:
                ans.append(arr[r])
                r-=1

        return ans            
        