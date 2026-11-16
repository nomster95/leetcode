class Cashier:

    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount = discount
        self.freq = {}
        self.products = products
        self.prices = prices
        
        for i in range(len(self.prices)):
            self.freq[self.products[i]] = self.prices[i]

        self.index = 0    
        

    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.index+=1
        bill = 0
        for i in range(len(product)):
            bill+=self.freq[product[i]]*amount[i]

        if self.index%self.n==0:
            bill = ((100-self.discount)/100)*bill

        return bill     
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)