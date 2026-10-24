class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adjlist = []
        for _ in range(n+1):
            adjlist.append([])

        for a,b in dislikes:
            adjlist[a].append(b) 
            adjlist[b].append(a)

        V = len(adjlist)
        color = [-1]*V

        def dfs(node,col):
            color[node] = col

            for nei in adjlist[node]:
                if color[nei]==-1:
                    # color every neighbor with opp color
                    result = dfs(nei,1-col)
                    if result==False:
                        return False
                    
                elif color[nei] == col:
                    return False

            return True

        # for checking every component    
        for i in range(V):
            if color[i]==-1:
                if not dfs(i,0):
                    return False

        return True                                
     

        
        