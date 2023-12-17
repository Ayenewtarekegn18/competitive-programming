class ATM:

    def __init__(self):
 	    self.cash = [0 for i in range(5)]
 	    self.value = [20,50,100,200,500]

    def deposit(self, dep: List[int]) -> None:
        for i in range(len(dep)):
            self.cash[i] += dep[i] 

    def withdraw(self, amount: int) -> List[int]:
        res = [0 for i in range(5)]
        for i in range(4,-1,-1):
            cash = self.cash[i]
            value = self.value[i]
            noOfNotes = min(cash,amount//value)
            res[i] = noOfNotes
            amount -= (noOfNotes*value)
        if amount == 0:
            self.deposit([-i for i in res])
            return res
        else:
            return [-1]

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)