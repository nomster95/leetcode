class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        freq = {}
        for i in range(len(messages)):
            if senders[i] not in freq:
                freq[senders[i]] = len(messages[i].split())
            else:
                freq[senders[i]]+=len(messages[i].split())

        max_count = 0
        b_sender = ""
        for sender,count in freq.items():
            if count>max_count or (count==max_count and sender>b_sender):
                max_count = count
                b_sender = sender

        return b_sender        




        