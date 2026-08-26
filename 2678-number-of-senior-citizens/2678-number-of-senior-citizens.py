class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = 0
        for i in details:
            age = i[11] + i[12]
            if int(age)>60:
                senior+=1

        return senior        
        