class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        freq = {}
        ans = set()
        for i in range(len(keyName)):
            name = keyName[i]
            time = keyTime[i]

            hours = int(time[0])*10+int(time[1])
            minutes = int(time[3])*10+int(time[4])

            total = hours*60 + minutes

            if name not in freq:
                freq[name] = []

            freq[name].append(total)

        for i in freq:
            arr = freq[i]
            arr.sort()
            if len(arr)>=3:
                for k in range(len(arr)-2):
                    if arr[k+2]-arr[k]<=60:
                        if i not in ans:
                            ans.add(i)

                        


        final = sorted(ans)

        return final               


        