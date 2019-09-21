#encode:utf8
import pandas as pd
import csv

class csvfile:
    def __init__(self, filename=None):
        self.filename = filename

    # print content in file with lines
    def readfile(self):
        content = []
        with open(self.filename, 'r', encoding='utf8') as f:
            for line in f.readlines():
                print(line.strip())
                content.append(line.strip())
        return content

    def readmatrix(self):
        content = []
        with open(self.filename, 'r', encoding='utf8') as f:
            for line in f.readlines():
                line = line.strip().split()
                print(line)
                content.append([int(i) for i in line])
        return content

    def csv2pd(self):
        if not self.iscsvfile():
            return None
        content = pd.read_csv(self.filename, encoding='gbk', sep=',', skiprows=0, nrows=None, )
        return content

    def csv2list(self):
        if not self.iscsvfile():
            return
        with open(self.filename, encoding='gbk') as f:
            rows = csv.reader(f, delimiter=',')
            for row in rows:
                print(row)
        return rows

    def iscsvfile(self):
        if not self.filename:
            return False
        if len(self.filename) < 5:
            return False
        if self.filename[-4:] == '.csv':
            return True
        return False


if __name__ == '__main__':
    file1 = file('/Users/duanyanling/Desktop/lanzhongbishidaan/sales_data_month1.csv')
    content = file1.csv2list()
    print(type(content))
