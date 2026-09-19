class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if xCenter < x1:
            closest_x_point = x1
        elif xCenter > x2:
            closest_x_point = x2
        else:
            closest_x_point = xCenter

        if yCenter < y1:
            closest_y_point = y1
        elif yCenter > y2:
            closest_y_point = y2
        else:
            closest_y_point = yCenter    



        distance = (((closest_x_point-xCenter)**2)+((closest_y_point-yCenter)**2))
        if distance<=radius**2:
            return True

        return False    
        