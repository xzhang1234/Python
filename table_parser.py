import csv
import re

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def create_table(data):
    col1 = []
    col2 = []
    col3 = []
    for row in data:
        col1.append(re.compile("(\d+)[a-zA-Z]").match(row[0]).group(1))
        col2.append(re.compile("\d+([a-zA-Z ]+)").match(row[0]).group(1))
        col3.append(row[1])
    return [col1, col2, col3]


def write_csv(filename, columns):
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(0, len(columns[0])):
            writer.writerow([columns[0][i], columns[1][i], columns[2][i]])

if __name__ == '__main__':
    columns = create_table(read_csv('old.csv'))
    write_csv('new.csv', columns)
