from _datetime import datetime
import csv

current_formatted_date = datetime.now().strftime("%Y-%m-%d")
exported_file_name = current_formatted_date + "-watchlist.csv"
market000name = "000market"


def parse_csv(csv_file_name):
    symbols_set = set()
    with open(csv_file_name, "r") as csv_file:
        # csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in csv_file:
            if row is None or len(row) == 0 or "000market".lower() in row.lower() or len(row.strip()) == 0 or \
                    len(row.split(",")[0].strip()) == 0:
                continue
            symbols_set.add(row.split(",")[0].strip())
    return symbols_set


def compare():
    updated_symbols = parse_csv(market000name)
    print("total updated :" + str(len(updated_symbols)))

    exported_symbols = parse_csv(exported_file_name)
    print("total exported :" + str(len(exported_symbols)))

    diff_set = set()
    for symbol in updated_symbols:
        if symbol not in exported_symbols:
            diff_set.add(symbol)

    print("total difference :" + str(len(diff_set)))

    common_set = updated_symbols.intersection(exported_symbols)
    print("total common :" + str(len(common_set)))

    for name in diff_set:
        print(name)


if __name__ == '__main__':
    compare()

