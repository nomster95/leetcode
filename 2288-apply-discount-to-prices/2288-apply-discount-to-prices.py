class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        ans = []
        for i in words:
            if i and i[0]=="$":
                st = i[1:]
                if st.isdigit():
                    x = int(st)
                    new_x  = ((100-discount)/100)*x
                    final = f"${new_x:.2f}"
                    ans.append(final)
                else:
                    ans.append(i)


            else:
                ans.append(i)

        return ' '.join(ans)        


        