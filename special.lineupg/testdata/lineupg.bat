@echo off
if "%1"=="" goto loop
copy lineupg%1.in lineupg.in >nul
echo Problem Test
echo Data %1
time<enter
lineupg
time<enter
fc lineupg.out lineupg%1.out
del lineupg.in
del lineupg.out
pause
goto end
:loop
for %%i in (1 2 3 4 5 6 7 8 9 10) do call %0 %%i
:end
