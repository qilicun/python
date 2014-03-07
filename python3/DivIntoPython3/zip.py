#!/usr/bin/env python3

import gzip

with gzip.open('out.log.gz', mode = 'wb') as z_file:
    z_file.write('A nine mile walk is no joke, especially in the rain.', encoding('utf-8'))
    exit()


