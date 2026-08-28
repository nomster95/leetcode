class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        AP = True
        for i in range(len(arr)-2):
            if arr[i+1]-arr[i] != arr[i+2]-arr[i+1]:
                AP = False

        return AP        
        