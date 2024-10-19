@echo off
setlocal enabledelayedexpansion

:: Define the root directory to start the search
set "rootDir="

:: Search for all files named "data" recursively and read them
for /r "%rootDir%" %%f in (data) do (
    echo Reading file: %%f
    type "%%f"
)

endlocal
