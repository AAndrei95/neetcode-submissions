class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = tickets[k]

        for i in range(len(tickets)):
            if tickets[i] < tickets[k] and i != k:
                time += tickets[i]
            elif tickets[i] >= tickets[k] and i < k:
                time += tickets[k]
            elif tickets[i] >= tickets[k] and i > k:
                time += tickets[k] - 1

        return time

        