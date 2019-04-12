# mkdirs
import sys
import os
import glob

def mkd(paths="ex1/",start=1,end=16,iscreatefile=True):
    for i in range(start,end):
        cpaths = paths+"c%02d" % i
        print(cpaths)
        #os.mkdir(cpaths)
        if os.path.exists(cpaths) is not True:
            os.mkdir(cpaths)
        if iscreatefile:
            for of in glob.glob(cpaths.replace("ex1","cookbook")+"/*.py"):
                print(of)
                #os.mknod(of.replace("cookbook","ex1"))
                if os.path.exists(of.replace("cookbook","ex1")) is not True:
                    with open(of.replace("cookbook","ex1"),"w") as f:
                        f.write("#!/usr/bin/env python3\n# -*- encoding: utf-8 -*-")

            
    


if __name__ == "__main__":
    mkd()
