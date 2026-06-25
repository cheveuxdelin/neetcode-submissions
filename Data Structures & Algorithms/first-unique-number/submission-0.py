class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniques = {}
        self.duplicates = set()

        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        if self.uniques:
            return next(iter(self.uniques))
        return -1
        

    def add(self, value: int) -> None:
        if value not in self.duplicates:
            if value in self.uniques:
                self.uniques.pop(value)
                self.duplicates.add(value)
            else:
                self.uniques[value] = True
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
