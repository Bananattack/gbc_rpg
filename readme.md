Dungeon Crawler (GameBoy Color homebrew)
----------------------------------------
*by Overkill and Kramlack*

Details:
* Title - To be announced.
* Release Date - To be announced.
* Platform - Game Boy Color.

A short and sweet old-school RPG for the Game Boy Color. Hoping to try some fun tricks on the Gameboy hardware, and make a fun game out of it. Written in Z80 assembly, compiled with RGBDS, some command-line utilities are written in Python. It's got a while to go still, but we have scrolling, textboxes, some menus, and a few art assets.

Build Requirements
------------------
* Python 2.7
* PIL

How to Build
------------

Run `build.bat`. When it successfully compiles, you should have a `hello.gb` file to run and play with. Enjoy!

Compatibility
-------------
* BGB - Should work in both Game Boy Color and Game Boy system settings. It should run free of exceptions if you turn on the breakpointing listed there.
* Physical hardware - Seems to work pretty normal on a Game Boy Color. Not sure about Game Boy.
* Visual Boy Advance - Should work, but there seem to be some bugs regarding how it handles LCDC flags to turn off the display. I will try to work around this as much as possible, since it is a fairly popular emulator.
* no$gb - Currently does not work due to some failed checksums, but it would be nice to get it working there.

License
-------
Copyright (C) 2011 Andrew G. Crowell (Overkill) and Kale Kramlack (Kramlack).

All work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/).