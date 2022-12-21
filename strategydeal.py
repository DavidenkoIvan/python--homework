class StrategyDeal(object):
    def __init__(self, bank, pair, option, entry, target, close):
        self.bank = bank
        self.pair = pair
        self.option = option
        self.entry = entry
        self.target = target
        self.close = close

    def get_target_percents(self):
        percent_target = [self.bank / self.entry * self.target[x] / 100 for x in range(len(self.target))]
        persents = [round(x, 2) for x in percent_target]
        return persents

    def get_targets(self):
        target_prices = [self.target[x] for x in range(len(self.target))]
        return target_prices

    def get_target_banks(self):
        target_banks = [self.bank / 10 * self.bank / self.entry * self.target[x] / 100 for x in range(len(self.target))]
        banks = [round(x, 2) for x in target_banks]
        return banks

    def get_size(self):
        size = [self.bank / StrategyDeal.get_targets(self)[x] for x in range(len(self.target))]
        sizes = [round(x, 2) for x in size]
        return sizes
    
    def __str__(self):
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\nPAIR: {self.pair} \n\n1 target: {StrategyDeal.get_targets(self)[0]}\nPercent: 
{StrategyDeal.get_target_percents(self)[0]}%\nBank: {StrategyDeal.get_target_banks(self)[0]}\nTarget size: {StrategyDeal.get_size(self)[0]}\n\n2 target: 
{StrategyDeal.get_targets(self)[1]}\nPercent: {StrategyDeal.get_target_percents(self)[1]}%\nBank: {StrategyDeal.get_target_banks(self)[1]}\nTarget size: 
{StrategyDeal.get_size(self)[1]}\n\n3 target: {StrategyDeal.get_targets(self)[2]}\nPercent: {StrategyDeal.get_target_percents(self)[2]}%\nBank: 
{StrategyDeal.get_target_banks(self)[2]}\nTarget size: {StrategyDeal.get_size(self)[2]}"