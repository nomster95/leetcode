class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        for i in range(len(asteroids)):
            while st and st[-1]>0 and asteroids[i]<0:
                diff = asteroids[i] + st[-1]
                if diff<0:
                    st.pop()
                elif diff>0:
                    asteroids[i] = 0
                else:
                    asteroids[i] = 0
                    st.pop()

            if asteroids[i]:
                st.append(asteroids[i])

        return st                        
                
                

                

                
        