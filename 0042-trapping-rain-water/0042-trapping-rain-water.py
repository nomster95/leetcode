class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        prefMax = [0]*len(height)
        suffMax = [0]*len(height)
        prefMax[0] = height[0]
        suffMax[n-1] = height[n-1]
        for i in range(1,n):
            prefMax[i] = max(prefMax[i-1],height[i])

        for i in range(n-2,-1,-1):
            suffMax[i] = max(suffMax[i+1],height[i])

        for i in range(n):
            leftMax = prefMax[i]
            rightMax = suffMax[i]
            if height[i]<leftMax and height[i]<rightMax:
                water+= min(leftMax,rightMax) - height[i]

        return water    
