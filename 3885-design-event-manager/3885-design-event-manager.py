import heapq
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.events = events
        self.h = []
        self.priority = {}
        for i,x in self.events:
            heapq.heappush(self.h,(-x,i))
            self.priority[i] = -x




        
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        heapq.heappush(self.h,(-newPriority,eventId))
        self.priority[eventId] = -newPriority
        

    def pollHighest(self) -> int:
        while self.h:
            neg_priority,eventid = heapq.heappop(self.h)

            if eventid in self.priority and  self.priority[eventid] == neg_priority:
                del self.priority[eventid]
                return eventid

        return -1        

         
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()