from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCounter = Counter("balloon")
        textCounter = Counter(text)
        count = float("inf")

        for char, freq in balloonCounter.items():
            count = min(count, textCounter[char] / freq)

        return int(count)  