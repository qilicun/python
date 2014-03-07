#!/use/bin/env python

with open('test.log', mode = 'w', encoding = 'utf-8') as file:
    file.write('test succecde!')

with open('test.log', encoding = 'utf-8') as file:
    print(file.read())

import subprocess
eval("subprocess.getoutput('rm test.log')")
