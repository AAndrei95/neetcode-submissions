class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        times = []
        lastOrder = customers[0][0]

        for arrival, time in customers:
            if lastOrder < arrival:
                lastOrder = arrival + time
                times.append(lastOrder-arrival)
            else:
                lastOrder = lastOrder + time
                times.append(lastOrder-arrival)

        return sum(times) / n
        