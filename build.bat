IF EXIST hello.obj del hello.obj
IF EXIST hello.sym del hello.sym
IF EXIST hello.map del hello.map
IF EXIST hello.gb del hello.gb
IF EXIST a.chr del a.chr
IF EXIST a.zhr del a.zhr

python tools/img2gb.py -oldfart resources/tiles/a.png
IF ERRORLEVEL 1 GOTO Done
python tools/img2gb.py resources/tiles/b.png
IF ERRORLEVEL 1 GOTO Done
python tools/textgen.py resources/text/messages.txt
IF ERRORLEVEL 1 GOTO Done

tools\pucrunch -d -c0 resources/tiles/b.chr resources/tiles/b.zhr
IF ERRORLEVEL 1 GOTO Done

tools\rgbasm -ohello.obj code/main.z80
IF ERRORLEVEL 1 GOTO Done
tools\xlink -mhello.map -nhello.sym xlink.cfg
IF ERRORLEVEL 1 GOTO Done
tools\rgbfix -p -v hello.gb

IF EXIST hello.obj del hello.obj
IF EXIST hello.sym del hello.sym
IF EXIST hello.map del hello.map

:Done
pause