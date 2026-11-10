class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:


        t = 1
        while t<=memory1 or t<=memory2:
            if memory1>memory2:
                memory1-=t
            elif memory1<memory2:
                memory2-=t
            else:
                memory1-=t

            t+=1

        return [t,memory1,memory2]                
        