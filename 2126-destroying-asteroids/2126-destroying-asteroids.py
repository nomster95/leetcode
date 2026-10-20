class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        n = len(asteroids)
        asteroids.sort()
        gain = mass
        for i in range(n):
            if gain>=asteroids[i]:   
                gain+=asteroids[i]
            else:
                return False

        return True            

        