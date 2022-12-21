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
            entry = float(splitted[i].lstrip('Вход: '))
        elif i == 4:
            target = list(map(float, splitted[i].lstrip('Таргет: ').split('; ')))
        elif i == 5:
            close = float(splitted[i].lstrip('Выход: '))
    data = bank, pair, option, entry, target, close
    return data