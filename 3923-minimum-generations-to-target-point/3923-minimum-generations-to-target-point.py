class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        k = 0

        points = [tuple(p) for p in points]    
        seen  = set(points)
        if tuple(target) in seen:
            return 0
        while tuple(target) not in seen:
            old_points = points[:]
            new_points = set()    
            for i in range(len(points)):
                for j in range(i+1,len(points)):
                    new_point = ((points[i][0]+points[j][0])//2,(points[i][1]+points[j][1])//2,(points[i][2]+points[j][2])//2)
                    new_points.add(new_point)
            k+=1

            old_size = len(seen)   

            for p in new_points:
                if p not in seen:
                    seen.add(p)
                    points.append(p)

                

            if len(seen)==old_size:
                return -1        


        return k        




        