#!/bin/env python
import array
import itertools
import os
import os.path
import sys

import PIL.Image

if __name__ == '__main__':
    CELL_WIDTH = False
    CELL_HEIGHT = False
    OUT_COLUMNS = False

    if len(sys.argv) > 1:
        for arg in range(1, len(sys.argv)):
            filename = sys.argv[arg]
        
            if filename[0] == '-':
                if filename.startswith('-w='):
                    CELL_WIDTH = int(filename.split('=')[1])
                elif filename.startswith('-h='):
                    CELL_HEIGHT = int(filename.split('=')[1])
                elif filename.startswith('-outcols='):
                    OUT_COLUMNS = int(filename.split('=')[1])
                else:
                    exit('Invalid argument `' + filename + '`.')
                continue

            if not CELL_WIDTH:
                exit('width not specified before filename!')
            if not CELL_HEIGHT:
                exit('width not specified before filename!')
            
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
            columns = w / (CELL_WIDTH + 1)
            rows = h / (CELL_HEIGHT + 1)

            OUT_COLUMNS = OUT_COLUMNS or columns
            print(OUT_COLUMNS)

            data = img.load()

            output_image = PIL.Image.new('RGB', (OUT_COLUMNS * CELL_WIDTH, ((rows * columns) / OUT_COLUMNS + 1) * CELL_HEIGHT))
            output_data = output_image.load()

            out_col = 0
            out_row = 0

            try:
                for y in range(0, rows):
                    for x in range(0, columns):
                        for j in range(0, CELL_HEIGHT):
                            for i in range(0, CELL_WIDTH):
                                p = data[x * (CELL_WIDTH + 1) + 1 + i, y * (CELL_HEIGHT + 1) + 1 + j]
                                output_data[out_col * CELL_WIDTH + i, out_row * CELL_HEIGHT + j] = p
                        out_col += 1
                        if out_col >= OUT_COLUMNS:
                            out_col = 0
                            out_row += 1
            except:
                import traceback
                print(sys.exc_info()[1])
                traceback.print_tb(sys.exc_info()[2])
                print('fuck', columns, rows, (rows * columns), x, y, i, j, out_col, out_row, OUT_COLUMNS, output_image.size[0], output_image.size[1])

            save_filename = os.path.splitext(filename)[0] + '.unborder.png'
            output_image.save(save_filename)
