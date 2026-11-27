from collections import deque
class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        if k>=len(arr):
            return max(arr)

        dq = deque(arr)
        prev_winner = max(arr[0],arr[1])
        streak = 0
        
        while streak!=k:
                x = dq.popleft()
                y = dq.popleft()
                if x>y:
                    dq.append(y)
                    dq.appendleft(x)
                else:
                    dq.append(x)
                    dq.appendleft(y)

                winner = dq[0]
                if winner==prev_winner:
                    streak+=1
                else:
                    prev_winner = winner
                    streak = 1

        return winner




        
