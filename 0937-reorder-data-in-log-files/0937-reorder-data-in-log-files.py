class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []
        for ch in logs:
            x = ch.split(" ")
            if x[1].isdigit():
                digit_logs.append(ch)
            else:
                letter_logs.append(ch)


        sorted_letter_logs = sorted(letter_logs , key=lambda x:(x.split()[1:],x.split()[0]))

        return sorted_letter_logs + digit_logs     





        