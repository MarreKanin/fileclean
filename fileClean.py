# -*- coding: utf-8 -*-
import os
from fnmatch import fnmatch
from datetime import datetime, timedelta
import datetime
import time


def main():
    root = 'C:\\Users\\'+os.getlogin()+'\\Desktop'
    pattern = "*.*"
    whitelist = ['.lnk', '.py']
    filelist = []
    folderlist = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                filelist.append((path + "\\" + name))
        if path not in folderlist:
            folderlist.append(path)
    newilelist = {}
    counter = 0
    for item in filelist:
        newilelist[counter] = str(item), time.strftime('%Y.%m.%d %H:%M:%S', time.gmtime(os.path.getmtime(item))), ('{:,.000f}'.format(os.path.getsize(item)/float(1 << 10))+" KB")
        counter += 1

    for x in newilelist:
        now = (datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"))
        nownow = (datetime.datetime.today().date() - datetime.timedelta(days=5)).strftime("%Y.%m.%d %H:%M:%S")

        if newilelist[x][1] < nownow and "."+str(newilelist[x][0].split('.')[-1]) not in whitelist:
            try:
                os.remove(newilelist[x][0])
                print('Removing ' + newilelist[x][0])
            except Exception as e:
                print(e)

    folderlist.pop(folderlist.index(root))
    for path in folderlist:
        if os.listdir(path) == []:
            os.rmdir(path)
            print("removing "+path)


if __name__ == "__main__":
    main()
