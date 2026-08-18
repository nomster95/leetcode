class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        
        for i in range(len(restaurants)):
            if veganFriendly==1:

                if restaurants[i][2]==1 and restaurants[i][3]<=maxPrice and restaurants[i][4]<=maxDistance:
                    ans.append([restaurants[i][0],restaurants[i][1]])

            else:
                if restaurants[i][3]<=maxPrice and restaurants[i][4]<=maxDistance:
                    ans.append([restaurants[i][0],restaurants[i][1]])



        ans.sort(key=lambda x: (x[1],x[0]),reverse = True)

        
        return [i[0] for i in ans]  

        

                

                

        