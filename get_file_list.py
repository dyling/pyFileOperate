import os


class ts:
    def __init__(self, dir):
        self.filelist = []
        self._deal_process(dir)

    def _deal_process(self, d):
        if d is not None:
            if os.path.isdir(d):
                print(d, ' is dir')
                dl = os.listdir(d)
                for l in dl:
                    t = d + '/' + l
                    self._deal_process(t)
            elif os.path.isfile(d):
                print(d, ' is file')
                self.filelist.append(d)
            else:
                print(d, ' is not dir add not file')
        else:
            print('deal over')

    def print_file(self):
        print("print file:", self.filelist.__len__())
        for f in self.filelist:
            print(f)


if __name__ == "__main__":
    ts('.').print_file()

    
    
