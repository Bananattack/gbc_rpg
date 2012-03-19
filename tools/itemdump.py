import os
import dat
import sys

worked = False
format = False
output = False

def usage(msg=None):
    if msg:
        sys.stderr.write(msg + '\n')
    sys.stderr.write('Usage: ' + sys.argv[0] + ' --format=FORMAT [OPTIONS] PREFIX\n')
    sys.stderr.write('  FORMAT: One of ' + repr(dat.DUMPERS.keys()) + '\n')
    sys.stderr.write('  PREFIX: The path of the file, sans extension.\n')
    sys.stderr.write('          There must be `PREFIX.def` and `PREFIX.dat`.\n')
    sys.stderr.write('  OPTIONS: Other parameters:\n')
    sys.stderr.write('    --out=FILENAME  A filename to write the parsed format into.\n')
    exit(1)

def set_format(key, val):
    global format
    if val is None:
        usage('Invalid usage `' + key + '`. Should be of form: `' + key + '=VALUE`')
    else:
        format = val

def set_output(key, val):
    global output
    if val is None:
        usage('Invalid usage `' + key + '`. Should be of form: `' + key + '=VALUE`')
    else:
        output = val

def unknown(key, val):
    if val is not None:
        usage('Unknown argument `' + key + '=' + val + '`')
    else:
        usage('Unknown argument `' + key + '`')

FLAGS = {
    '--format': set_format,
    '--out': set_output,
}

for arg in sys.argv[1:]:
    if arg.startswith('--'):
        arg = arg.split('=')
        if len(arg) == 1:
            key, val = arg, None
        elif len(arg) == 2:
            key, val = arg
        FLAGS.get(key, unknown)(key, val)

for arg in sys.argv[1:]:
    if not arg.startswith('--'):
        if not format:
            usage('Missing `--format` argument.')
        if not os.path.exists(arg + '.def'):
            usage('Missing definition file "' + arg + '.def' + '"')
        if not os.path.exists(arg + '.dat'):
            usage('Missing data file "' + arg + '.dat' + '"')

        dump = dat.Dat(arg + '.dat', arg + '.def').dump(format)
        if output:
            try:
                f = open(output, 'w')
            except Exception as e:
                exit('Failure attempting to write ' + output)
            f.write(dump + '\n')
            f.close()
        else:
            print(dump)
        worked = True
        break

if not worked:
    usage()
