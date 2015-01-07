import os
def walk_dir(dir,fileinfo,topdown=True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            print(os.path.join(name))
            fileinfo.write(os.path.join(root,name) + '\n')
        for name in dirs:
            print(os.path.join(name))
            fileinfo.write('  ' + os.path.join(root,name) + '\n')
dir = raw_input('please input the path:')
dir = r'/private/miliu/utchem-new/utchem2013_12A-package/source code-utchem2013_12A'
fileinfo = open('list2.txt','w')
walk_dir(dir,fileinfo)
