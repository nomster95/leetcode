class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        points1 = 0
        points2 = 0
        player1 = True
        player2 = False
        for i in range(len(nums)):
            if nums[i]%2!=0 and (i+1)%6==0:
                player1,player2 = player2,player1
                player1,player2 = player2,player1
            elif nums[i]%2!=0 or  (i+1)%6==0:
                player1,player2 = player2,player1
            

            if player1:
                points1+=nums[i]
            elif player2:
                points2+=nums[i]

        return points1 - points2                

        