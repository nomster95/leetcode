class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        ans = []
        nearest = 101
        index = -1
        tx = target[0]
        ty = target[1]
        for i in range(len(drones)):
            dist = abs(drones[i][0]-tx) + abs(drones[i][1]-ty)
            if dist<=drones[i][2]:
                ans.append([dist,i])

        for x,i in ans:
            if x<nearest:
                nearest = x
                index = i
            elif x==nearest and i<index:
                index = i

        return index                    

        