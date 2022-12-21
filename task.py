def read_data(file_name):
    with open(file_name) as f:
        rows = f.read()
        return rows


def write_data(out):
    with open('out.txt', 'w') as f:
        out_file = f.write(out)
        return out_file


content = read_data('input.txt')