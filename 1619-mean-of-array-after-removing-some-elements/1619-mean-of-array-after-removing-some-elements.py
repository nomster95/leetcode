class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        x = int(len(arr)*(5/100))
        i = 0
        j = len(arr)-1
        new = arr[i+x:j-x+1]
        mean = sum(new)/len(new)
        return mean


        
        