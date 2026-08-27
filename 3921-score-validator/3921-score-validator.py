class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        runs = 0
        wickets = 0
        for i in events:
            if wickets==10:
                return [runs,wickets]
            if i.isdigit():
                runs+=int(i)
            elif i=='W':
                wickets+=1   
            elif i=='NB' or i=='WD':
                runs+=1

        return [runs,wickets]             
        