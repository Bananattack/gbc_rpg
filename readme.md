Dungeon Crawler (Game Boy Color homebrew)
=========================================
***by Overkill (code) and Kramlack (art)***

A short and sweet old-school RPG for the Game Boy Color. Hoping to try some fun tricks on the Gameboy hardware, and make a fun game out of it. Written in Z80 assembly, compiled with RGBDS, some command-line utilities are written in Python. It's got a *while* to go still, but we have some of the preliminary systems in: scrolling, textboxes, some menus, and a few art assets. I would say it's about super-early pre-alpha tech demo stage at the moment, not feature complete by any means.

Build Requirements
------------------
* Python 2.7
* PIL
* RGBDS (Windows version included). For other platforms [this assembler](https://github.com/bentley/rgbds) might be able to build it.

How to Build
------------
On Windows, run `build.bat` When it successfully compiles, you should have a `hello.gb` file to run and play with. Enjoy!

Hardware Compatibility
----------------------
* Game Boy - ?
* Game Boy Advance - ?
* Game Boy Advance SP - ?
* Game Boy Color - Seems to work well, so far (Thanks Kramlack for trying it). This is the primary intended platform, but it should work on other GB hardware as well.
* Game Boy Pocket - ?
* Super Game Boy - ?

Emulator Compatibility
----------------------
* BGB - Should work in both Game Boy Color and Game Boy system settings. It should run free of exceptions if you turn on the breakpointing listed there.
* Visual Boy Advance - Should work, but there seem to be some bugs regarding how it handles LCDC flags to turn off the display. I will try to work around this as much as possible, since it is a fairly popular emulator.
* no$gb - Currently does not work due to some failed checksums, but it would be nice to get it working there.

License
-------
Copyright (C) 2011 Andrew G. Crowell (Overkill) and Kale Kramlack (Kramlack).

All work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/).