class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.freq = {}
        

    def setCell(self, cell: str, value: int) -> None:
        self.freq[cell] = value

        

    def resetCell(self, cell: str) -> None:
        self.freq[cell] = 0
        

    def getValue(self, formula: str) -> int:
        ans = 0
        s = formula.split("+")
        x = s[0][1:]
        y = s[1]
        if x.isdigit():
            ans+=int(x)
        else:
            if x in self.freq:
                ans+=self.freq[x]


        if y.isdigit():
            ans+=int(y)
        else:
            if y in self.freq:
                ans+=self.freq[y]


        return ans            

        

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)