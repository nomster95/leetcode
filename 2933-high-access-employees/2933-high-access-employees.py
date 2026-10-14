class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        freq = {}
        ans = set()
        for i in range(len(access_times)):
            name = access_times[i][0]
            time = access_times[i][1]

            hours = int(time[0])*10+int(time[1])
            minutes = int(time[2])*10+int(time[3])

            total = hours*60 + minutes

            if name not in freq:
                freq[name] = []

            freq[name].append(total)

        for i in freq:
            arr = freq[i]
            arr.sort()
            if len(arr)>=3:
                for k in range(len(arr)-2):
                    if arr[k+2]-arr[k]<60:
                        if i not in ans:
                            ans.add(i)

                        


        return list(ans)         

        