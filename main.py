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