import os
import re
import csv
# import shutil
import win_unicode_console
win_unicode_console.enable()

wantFileType = ['.mp4', '.rmvb', '.avi', '.mkv']


class operFileCsv():
    def __init__(self, filename=None):
        self.filename = filename

    def readCsvFile(self):
        readCsvHandler = open(self.filename, 'r')
        filelines = csv.reader(readCsvHandler, dialect='excel')
        for fileline in filelines:
            print(fileline)
        readCsvHandler.close

    def writeCsvFile(self, writeline):
        writeCsvHandler = open(self.filename, 'a', newline='')
        csvWrite = csv.writer(writeCsvHandler, dialect='excel')
        csvWrite.writerow(writeline)
        writeCsvHandler.close()


class findFileClass():
    def __init__(self, directer=""):
        self.dir = directer
        self.dirQueue = [self.dir]
        self.deal_process()

    # 1. cp file to self.dir
    # 2. make path to self.dirQueue
    def dealCurrentDir(self, currentDir):
        if not os.path.exists(currentDir):
            # print(currentDir, " is not exists.")
            return False
        contents = os.listdir(currentDir)
        # print(type(contents))  // list

        for content in contents:
            temppath = currentDir + "/" + content
            if os.path.isdir(temppath):
                self.enQueue(temppath)
            else:
                # print(content, " is a file.")
                try:
                    mediaType = re.search('\..*', content).group()
                except AttributeError as identifier:
                    print(identifier)
                    mediaType = None
                if mediaType in wantFileType:
                    yield self.dealWantFile(currentDir, content)

    def dealWantFile(self, dirWant, fileWant):
        # print(fileWant)
        # if not dirWant == self.dir:
        #     shutil.copyfile(dirWant + '/' + fileWant,
        #                     self.dir + "/" + fileWant)
        return dirWant, fileWant

    def enQueue(self, dir):
        self.dirQueue.append(dir)

    def popQueue(self):
        if not self.dirQueue:
            return None
        return self.dirQueue.pop()

    def deal_process(self):
        while True:
            # print("self.queue length is :", len(self.dirQueue))
            currentdir = self.popQueue()
            if not currentdir:
                print("Deal all content over.")
                return
            else:
                # print(currentdir)
                yield self.dealCurrentDir(currentdir)


class filecount:
    def __init__(self, filename=None):
        self.filename = filename

    def _files_number(self, pathname):
        num = 0
        if not os.path.exists(pathname):
            return 0
        elif os.path.isfile(pathname):
            return 1
        elif os.path.isdir(pathname):
            contents = os.listdir(pathname)
            for content in contents:
                newpath = os.path.join(pathname, content)
                if os.path.isfile(newpath):
                    num += 1
                elif os.path.isdir(newpath):
                    num += self._files_number(newpath)
        return num

    def get_number(self):
        return self._files_number(self.filename)


# oper: 1, return count of file;
#       2, return count of file belong to some type;
#       3, delete file belong to some type;
#       4, add string into file belong to some type.
class operfile:
    def __init__(self, filename=None, oper=0, filetype=None):
        self.filename = filename
        self.oper = oper
        self.filetype = filetype

    def _dealfile(self, filepath):
        if not os.path.isfile(filepath):
            return
        if not self.filetype:
            return
        if self.oper == 3:
            num = len(self.filetype)
            if filepath[-num:] == self.filetype:
                print('Delete file: [{0}].'.format(filepath))
                os.remove(filepath)
        elif self.oper == 4:
            num = len(self.filetype)
            if filepath[-num:] == self.filetype:
                print('Deal: [{0}].'.format(filepath))
                with open(filepath, 'a+') as f:
                    f.write('\n# git \n')

    def _find_files(self, pathname):
        num = 0
        if not os.path.exists(pathname):
            return 0
        elif os.path.isfile(pathname):
            return 1
        elif os.path.isdir(pathname):
            contents = os.listdir(pathname)
            for content in contents:
                newpath = os.path.join(pathname, content)
                if os.path.isfile(newpath):
                    if self.oper == 1:
                        num += 1
                    elif self.oper == 2:
                        if content[-3:] == self.filetype:
                            num += 1
                    else:
                        if content[-len(self.filetype):] == self.filetype:
                            num += 1
                        self._dealfile(newpath)
                elif os.path.isdir(newpath):
                    num += self._find_files(newpath)
        return num

    def deal_process(self):
        num = self._find_files(self.filename)
        print('The number of file is ', num)


if __name__ == "__main__":

    # filename = 'E:/C_yuyan/visual_studio_2015/Thermal_Power_FlaskWeb/FlaskWebProject4'
    # filename = 'E:/C_yuyan/visual_studio_code/dylLib/pyFileOperate'
    filename = 'E:/C_yuyan/visual_studio_2015/Thermal_Power_FlaskWeb/FlaskWebProject4'
    filename = 'E:/C_yuyan/visual_studio_2015/Thermal_Power_FlaskWeb/FlaskWebProject4/'
    deletetype = 'pyc'
    modifytype = '__init__.py'

    # operfile(filename=filename, oper=3, filetype=deletetype).deal_process()
    # operfile(filename=filename, oper=4, filetype=modifytype).deal_process()
    operfile(filename=filename, oper=1, filetype=modifytype).deal_process()

