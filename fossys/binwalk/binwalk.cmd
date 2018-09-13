@echo off
rem Wrapper batch for binwalk.exe to make it possible for binwalk to find
rem magic.binarch, magic.bincast, magic.binwalk and extract.conf in the same
rem directory than binwalk.exe.

pushd %CD%
cd %~dp0

break

start /B /W "BinWalk" %~dp0\binwalk.exe %*
popd
