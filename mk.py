# mkdirs
import sys
import os

def mkd(paths="ex1/",start=1,end=16):
    for i in range(start,end):
        print("%02d" % i)
        os.mkdir(paths+"%02d" % i)


if __name__ == "__main__":
    mkd()