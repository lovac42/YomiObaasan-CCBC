call :build_ui about
call :build_ui preferences
call :build_ui reader
exit


:build_ui
echo building %1.ui...

pyuic5 %1.ui -o out.py

type header.py >%1_ui.py

findstr /V "# PyQt5 resources_rc" out.py>>%1_ui.py

if /i not %1==updates echo from . import resources_rc>>%1_ui.py

del out.py
move %1_ui.py ..\src\yomi_obaasan\gen

exit /b
