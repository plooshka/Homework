from beautifultable import BeautifulTable


def str_range_list(x, y: int) -> list:
    range_list = list()
    for i in range(x, y+1):
        range_list.append(str(i))
    return range_list


def multipl_table(a, b, c, d: int):
    table = BeautifulTable()
    row = list()
    for i in range(a, b+1):
        for k in range(c, d+1):
            row.append(i*k)
        table.append_row(row)
        row.clear()
    table.rows.header = str_range_list(a, b)
    table.columns.header = str_range_list(c, d)
    print(table)


a = 2
b = 4
c = 3
d = 7


multipl_table(a, b, c, d)
