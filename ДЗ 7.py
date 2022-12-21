input.txt

BANK: 1000

APE-FTT

Покупка

Вход: 20.11

Таргет: 21.5; 22.8; 23.5

Выход: 19.0

BANK: 1000

out.txt

BANK: 1000.0
START_PRICE: 20.11
STOP_PRICE: 19.0
PAIR: APE-FTT 

1 target: 21.5
Percent: 10.69%
Bank: 1069.12
Target size: 46.51

2 target: 22.8
Percent: 11.34%
Bank: 1133.76
Target size: 43.86

3 target: 23.5
Percent: 11.69%
Bank: 1168.57
Target size: 42.55





from task_io import read_data, write_data
from strategy_deal import StrategyDeal
from utils import prepare


if __name__ == '__main__' :
    data = prepare(read_data('input.txt'))
    deal = StrategyDeal(*data)
    deal.get_target_percents()
    deal.get_targets()
    deal.get_target_banks()
    deal.get_size()
    out = deal.__str__()
    write_data(out)






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





def read_data(file_name):
    with open(file_name) as f:
        rows = f.read()
        return rows


def write_data(out):
    with open('out.txt', 'w') as f:
        out_file = f.write(out)
        return out_file


content = read_data('input.txt')








from task_io import content


def prepare(content):
    global bank, pair, option, entry, target, close
    splitted = list(filter(None, content.split('\n')))
    for i in range(len(splitted)):
        if i == 0:
            bank = float(splitted[i].lstrip('BANK: '))
        elif i == 1:
            pair = splitted[i]
        elif i == 2:
            option = splitted[i]
        elif i == 3:
            entry = float(splitted[i].lstrip('Âõîä: '))
        elif i == 4:
            target = list(map(float, splitted[i].lstrip('Òàðãåò: ').split('; ')))
        elif i == 5:
            close = float(splitted[i].lstrip('Âûõîä: '))
    data = bank, pair, option, entry, target, close
    return data
   
