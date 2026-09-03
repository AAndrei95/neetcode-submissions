import re

class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.chars = [x for x in self.compressedString if x.isalpha()]
        self.compressedBy = re.sub(r'[^0-9]', '.', self.compressedString).split(".")
        
        for space in self.compressedBy:
            if space == "":
                self.compressedBy.remove(space)


        self.idx = 0
        self.amount = int(self.compressedBy[self.idx])

        
    def next(self) -> str:
        char = self.chars[self.idx]
        self.amount -= 1

        if self.amount == 0 and self.idx < len(self.chars) - 1:
            self.idx += 1
            self.amount = int(self.compressedBy[self.idx])

        return char

    def hasNext(self) -> bool:
        return self.idx <= len(self.chars) - 1 and self.amount > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
