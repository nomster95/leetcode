class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # alice days:-
        alice_arrive_month = int(arriveAlice[0])*10 + int(arriveAlice[1])
        alice_leave_month = int(leaveAlice[0])*10 + int(leaveAlice[1])
        alice_arrive_day = int(arriveAlice[3])*10 + int(arriveAlice[4])
        alice_leave_day = int(leaveAlice[3])*10 + int(leaveAlice[4])

        #bob days:-
        bob_arrive_month = int(arriveBob[0])*10 + int(arriveBob[1])
        bob_leave_month = int(leaveBob[0])*10 + int(leaveBob[1])
        bob_arrive_day = int(arriveBob[3])*10 + int(arriveBob[4])
        bob_leave_day = int(leaveBob[3])*10 + int(leaveBob[4])

        days_in_month = [0,31,59,90,120,151,181,212,243,273,304,334]

        alice_arrive_days = days_in_month[alice_arrive_month-1] + alice_arrive_day
        alice_leave_days = days_in_month[alice_leave_month-1] + alice_leave_day

        bob_arrive_days = days_in_month[bob_arrive_month-1] + bob_arrive_day
        bob_leave_days = days_in_month[bob_leave_month-1] + bob_leave_day

        arrival = max(alice_arrive_days,bob_arrive_days)
        departure = min(alice_leave_days,bob_leave_days)

        if departure<arrival:
            return 0

        return departure-arrival+1    





        








        