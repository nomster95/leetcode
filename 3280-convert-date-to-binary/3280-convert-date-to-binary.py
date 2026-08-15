class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dates = date.split("-")

        year = bin(int(dates[0]))[2:]
        month = bin(int(dates[1]))[2:]
        day = bin(int(dates[2]))[2:]
        return f"{year}-{month}-{day}"


    
        
        