class Solution:
    def minRotations(self, n: int, s: str) -> int:
        
        moves = 0
        current = 0
        for x in s:
            target = int(x)
            d = abs(target-current)
            moves+=min(d,10-d)
            current = target


        total = moves

        for k in range(len(s)):
            if k==0:
                old = min(int(s[k]),10-int(s[k]))
                new = min(int(s[-1]),10-int(s[-1]))

                total = min(total,moves-old+new)

            else:
                d1 = abs(int(s[k-1])-int(s[k]))
                olds = min(d1,10-d1)

                d2 = abs(int(s[k-1])-int(s[-1]))
                news = min(d2,10-d2)

                total = min(total,moves-olds+news)

        return total     

                
            
                
                
            

        
        