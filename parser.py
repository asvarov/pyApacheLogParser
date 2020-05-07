import re
import csv
from collections import Counter

def reader(filename):
    with open(filename) as f:
        log = f.read()
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips_list = re.findall(regexp, log)
        return (ips_list)


def count(ips_list):
    counter = Counter(ips_list)
    result = Counter(ips_list).most_common(10)
    return counter


def write_csv(counter):
    with open('output.csv', mode='w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Frequency']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))


if __name__ == '__main__':
    filename = reader('log')
    counter = count(filename)
    write_csv(counter)
