#!/usr/bin/env python
import os
import sys
import subprocess

PRE_CLEAN = ['hello.obj', 'hello.sym', 'hello.map', 'hello.gb', 'a.chr', 'b.chr', 'b.zhr']

COMMANDS = [
    'python tools/img2gb.py -oldfart resources/tiles/a.png',
    'python tools/img2gb.py resources/tiles/b.png',
    'python tools/itemdump.py resources/data/items --format=z80 --out=resources/data/items.dmp',
    'python tools/itemdump.py resources/data/items --format=texts --out=resources/data/items.auto.txt',
    'python tools/textgen.py resources/data/items.auto.txt',
    'python tools/textgen.py resources/text/messages.txt',
    'tools/pucrunch -d -c0 resources/tiles/b.chr resources/tiles/b.zhr',
    'tools/rgbasm -ohello.obj code/main.z80',
    'tools/xlink -mhello.map -nhello.sym xlink.cfg',
    'tools/rgbfix -p -v hello.gb'
]

POST_CLEAN = ['hello.obj', 'hello.sym', 'hello.map']

sys.stderr.write('>> Pre-build Cleanup...\n')
for filename in PRE_CLEAN:
    try:
        os.remove(filename)
    except:
        pass

sys.stderr.write('>> Building...\n')
for command in COMMANDS:
    sys.stderr.write('-- `' + command + '` --\n')
    result = subprocess.call(command)
    if result:
        exit("\n*** Failed with error code {}.\n".format(result))

sys.stderr.write('>> Post-build Cleanup...\n')
for filename in POST_CLEAN:
    try:
        os.remove(filename)
    except:
        pass

sys.stderr.write('\nOK.\n')



