class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        track = set()
        score = 0
        n = len(instructions)
        i =0
        while i<n and i>=0:
            if i in track:
                break
            elif instructions[i]=="add":
                score+=values[i]
                track.add(i)
                i+=1
            elif instructions[i]=="jump":
                track.add(i)
                i = i + values[i]   

        return score         


        

        