from collections import deque
class RideSharingSystem:

    def __init__(self):
        self.rider = deque()
        self.driver = deque()
        

    def addRider(self, riderId: int) -> None:
        self.rider.append(riderId)
        

    def addDriver(self, driverId: int) -> None:
        self.driver.append(driverId)
        

    def matchDriverWithRider(self) -> List[int]:
        if len(self.rider)!=0 and len(self.driver)!=0:
            x = self.rider.popleft()
            y = self.driver.popleft()
            return [y,x]
        else:
            return [-1,-1]    

        

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.rider:
            self.rider.remove(riderId)
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)