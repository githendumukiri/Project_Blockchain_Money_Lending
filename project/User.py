class User:
    amountofusers = 0

    def __init__(self, username,starting_balance):
        self.username = username
        self.balace = starting_balance
        User.amountofusers += 1
        self.yournumberinline = User.amountofusers -1

    def receivemoney(self,amount):
        int_amount = int(amount)
        self.balace += int_amount

    def sendmoney(self,amount):
        int_amount = int(amount)
        self.balace -= int_amount
        return int_amount

    def getbalance(self):
        return self.balace

    def getaccountname(self):
        return self.username

    def getlinenumber(self):
            return self.yournumberinline