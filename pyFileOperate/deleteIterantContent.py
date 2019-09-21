# Put some line from filecsv2 into filecsv3 which not in filetxt1
# From git@github.com:dyling/deleteIterantFileContent.git 
import csv
from pyFileOperate.operFile import operFileCsv

filetxt1 = 'E:/gg/log/log1.txt'
filecsv2 = 'E:/gg/log/log2.csv'
filecsv3 = 'E:/gg/log/log3.csv'


class getLogBuffFromFile():
    def __init__(self):
        self.logBuff1 = []

    def getLog1Buff(self, filename):
        with open(filename) as filehandler:
            while True:
                logOneLine = filehandler.readline().strip()
                if not logOneLine:
                    break
                self.logBuff1.append(logOneLine)
        return self.logBuff1


class deleteIterantLog():
    def __init__(self):
        self.logBuff1List = None
        self.logBuff2OneLine = None

    def deleteProcedure(self, oldlog, newlog, createlog):
        self.logBuff1List = getLogBuffFromFile().getLog1Buff(oldlog)
        self.dealProcedure(newlog, createlog)

    def dealProcedure(self, file1name, file2name):
        with open(file1name, 'r') as readCsvHandler:
            filelines = csv.reader(readCsvHandler, dialect='excel')
            for fileline in filelines:
                if not fileline:
                    continue
                if fileline[0] not in self.logBuff1List:
                    operFileCsv(file2name).writeCsvFile(fileline)


if __name__ == '__main__':
    deleteIterantLog().deleteProcedure(filetxt1, filecsv2, filecsv3)
