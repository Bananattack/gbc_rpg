import os

PRE_CLEAN = ['hello.obj', 'hello.sym', 'hello.map', 'hello.gb', 'a.chr', 'b.chr', 'b.zhr']

COMMANDS = [
    '{python} tools/img2gb.py -oldfart resources/tiles/a.png',
    '{python} tools/img2gb.py resources/tiles/b.png',
    '{python} tools/itemdump.py resources/data/items --format=z80 --out=resources/data/items.dmp',
    '{python} tools/itemdump.py resources/data/items --format=texts --out=resources/data/items.auto.txt',
    '{python} tools/textgen.py resources/data/items.auto.txt',
    '{python} tools/textgen.py resources/text/messages.txt',
    os.path.join('{pucrunch_path}', 'pucrunch') + ' -d -c0 resources/tiles/b.chr resources/tiles/b.zhr',
    os.path.join('{rgbds_path}', 'rgbasm') + ' -ohello.obj code/main.z80',
    os.path.join('{rgbds_path}', 'rgblink') + ' -mhello.map -nhello.sym -ohello.gb hello.obj',
    os.path.join('{rgbds_path}', 'rgbfix') +' -p0 -v hello.gb'
]

POST_CLEAN = ['hello.obj', 'hello.sym', 'hello.map']

if __name__ == '__main__':
    import sys
    import subprocess

    if sys.version_info[:2] < (2, 7):
        exit('Insufficient python version (needs 2.7):\n' + sys.version)

    pucrunch_path = 'tools'
    rgbds_path = 'tools'

    def unknown(key, val):
        if val is not None:
            exit('Unknown argument `' + key + '=' + val + '`')
        else:
            exit('Unknown argument `' + key + '`')

    def set_pucrunch_path(key, val):
        global pucrunch_path
        if val is None:
            exit('Invalid usage `' + key + '`. Should be of form: `' + key + '=VALUE`')
        else:
            pucrunch_path = val

    def set_rgbds_path(key, val):
        global rgbds_path
        if val is None:
            exit('Invalid usage `' + key + '`. Should be of form: `' + key + '=VALUE`')
        else:
            rgbds_path = val

    FLAGS = {
        '--rgbds-bin': set_rgbds_path,
        '--pucrunch-bin': set_pucrunch_path,
    }

    for arg in sys.argv[1:]:
        if arg.startswith('--'):
            arg = arg.split('=')
            if len(arg) == 1:
                key, val = arg, None
            elif len(arg) == 2:
                key, val = arg
            FLAGS.get(key, unknown)(key, val)



    sys.stderr.write('>> Pre-build Cleanup...\n')
    for filename in PRE_CLEAN:
        try:
            os.remove(filename)
        except:
            pass

    sys.stderr.write('>> Building...\n')
    for command in COMMANDS:
        command = command.format(pucrunch_path=pucrunch_path, rgbds_path=rgbds_path, python=sys.executable)
        sys.stderr.write('-- `' + command + '` --\n')
        result = subprocess.call(command, shell=True)
        if result:
            exit("\n*** Failed with error code {}.\n".format(result))

    sys.stderr.write('>> Post-build Cleanup...\n')
    for filename in POST_CLEAN:
        try:
            os.remove(filename)
        except:
            pass

    sys.stderr.write('\nOK.\n')

