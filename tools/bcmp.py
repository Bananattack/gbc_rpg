#!/usr/bin/env python
import hashlib

def bcmp(a, b):
    print(len(a))
    print(len(b))
    
    h = hashlib.md5()
    h.update(a)
    
    h2 = hashlib.md5()
    h2.update(b)

    h = h.hexdigest()
    h2 = h2.hexdigest()

    return h == h2, h, h2

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 3:
        same, h, h2 = bcmp(file(sys.argv[1]).read(), file(sys.argv[2]).read())
    
        print('Same ({})'.format(h) if same else 'Different ({} vs {})'.format(h, h2))
    else:
        print('usage: ' + sys.argv[0] + ' a b')
        print('Compares two files, and returns whether they are equal.')