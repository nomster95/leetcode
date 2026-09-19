class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x_point = max(x1,min(xCenter,x2))
        closest_y_point = max(y1,min(yCenter,y2))

        distance = (((closest_x_point-xCenter)**2)+((closest_y_point-yCenter)**2))
        if distance<=radius**2:
            return True

        return False    
        