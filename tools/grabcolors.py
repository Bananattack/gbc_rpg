#!/bin/env python
import array
import itertools
import os
import os.path
import sys

import PIL.Image

if __name__ == '__main__':
    HUMAN = False

    if len(sys.argv) > 1:
        for arg in range(1, len(sys.argv)):
            filename = sys.argv[arg]
        
            if filename[0] == '-':
                if filename == '-human':
                    HUMAN = True
                else:
                    exit('Invalid argument `' + filename + '`.')
                continue
            
            try:
                img = PIL.Image.open(filename)
            except IOError as e:
                if os.path.isdir(filename):
                    exit(filename + ' is a directory.')
                if os.path.exists(filename):
                    exit(filename + ' has an unsupported filetype, or you lack permission to open it.')
                else:
                    exit('File ' + filename + ' does not exist!')
            
            w, h = img.size
            total_colors = 0
            pals = []
            
            if img.palette:
                # Paletted image containing a single palette.
                # Pass it along directly.
                type, data = img.palette.getdata()
                
                pal = array.array('B', data).tolist()
                pals.append(pal)
                
                total_colors += len(pal) // 3
            else:
                # RGB Image containing rows of colors.
                # Treat each unique row as a palette.
                data = img.load()
                rows = set()
                for y in range(h):
                    row = []
                    prev = None
                    for x in range(w):
                        c = data[x, y]
                        if prev != c:
                            prev = c
                            row.append(c)
                    
                    row = tuple(row)
                    
                    if row not in rows:
                        rows.add(row)
                        
                        pal = list(itertools.chain(*row))
                        pals.append(pal)
                        
                        total_colors += len(pal) // 3


            # Dump converted palette which can be used with GBC_RGB_DATA.
            if HUMAN:
                print('From {} ({}), found {} palettes, {} total colors.'.format(filename, img.palette and 'indexed' or 'rgb', len(pals), total_colors))
            else:
                print('; source {} ({}), {} palettes, {} total colors.'.format(filename, img.palette and 'indexed' or 'rgb', len(pals), total_colors))
            for i, pal in enumerate(pals):
                if HUMAN:
                    print('Palette #{}'.format(i))
                else:
                    print('; Palette {}'.format(i))
                
                for j in range(0, len(pal), 3):
                    sr, sg, sb = pal[j], pal[j + 1], pal[j + 2]
                    dr, dg, db = sr * 32 // 256, sg * 32 // 256, sb * 32 // 256
                    
                    if HUMAN:
                        print('  Color #{}: R={}, G={}, B={} (Original 24-bit value: R={}, G={}, B={},)'.format(j / 3, dr, dg, db, sr, sg, sb))
                    else:
                        print('DW ${:04X} ; #{:02X}{:02X}{:02X}'.format(dr | dg << 5 | db << 10, sr, sg, sb))
                    #print('    GBC_RGB_DATA ${:02X}, ${:02X}, ${:02X} ; #{:02X}{:02X}{:02X} -> ${:04X}'.format(dr, dg, db, sr, sg, sb, dr | dg << 5 | db << 10))
