import os
import os.path
import re

def parse_error(filename, line_number, message):
    exit('error: ' + filename + ':' + str(line_number) + ': ' + message)

translations = {
    '\n': 0x01,
    ' ': 0xCE,
    '_': 0xCE,
    'A': 0x80,
    'a': 0x9A,
    '0': 0xBC,
    '.': 0xB5,
    '!': 0xB6,
    '?': 0xB7,
    '\'': 0xB8,
    ',': 0xB4,
    ':': 0xC7,
    '/': 0xC6,
}
for c in range(ord('A'), ord('Z') + 1):
    translations[chr(c)] = c - ord('A') + translations['A']
for c in range(ord('a'), ord('z') + 1):
    translations[chr(c)] = c - ord('a') + translations['a']
for c in range(ord('0'), ord('9') + 1):
    translations[chr(c)] = c - ord('0') + translations['0']

support = ''.join(translations.keys())

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        for arg in range(1, len(sys.argv)):
            filename = sys.argv[arg]
            
            if filename[0] == '-':
                # TODO ARGUMENTS
                exit('Invalid argument `' + filename + '`.')
            
            f = open(filename, 'r')
            save_filename = os.path.splitext(filename)[0] + '.tdb'
            try:
                save_file = open(save_filename, 'w')
            except Exception as e:
                exit('Failure attempting to write ' + save_filename)

            for line_number, line in enumerate(f):
                if line.startswith('#'):
                    continue
                parts = line.split(':', 1)
                if not len(parts):
                    continue
                if len(parts) < 2:
                    parse_error(filename, line_number, 'found text without label')

                label = parts[0].strip()
                text = parts[1].strip()

                if not label:
                    parse_error(filename, line_number, 'invalid empty label encountered.')
                if re.match('^[a-zA-Z0-9_]+$', label) is None:
                    parse_error(filename, line_number, 'invalid label "' + label + '" -- should only contain the characters 0-9, a-z, A-Z, and _.')

                text = text.replace('|', '\n')
                bad = re.findall('[^' + support + ']', text)
                if len(bad):
                    parse_error(filename, line_number, 'unsupported text characters found:\n       ' + ''.join(set(bad)))

                output = []
                for c in text:
                    output.append('${:02X}'.format(translations[c]))
                output.append('0')
                save_file.write(label + ': DB ' + ', '.join(output) + '\n')
            
            print('  ' + filename + ' -> ' + save_filename)
                    
    else:
        print('Usage: ' + sys.argv[0] + ' file [file...]')
        print('Converts text files into assemblies containing labelled tile data.')
