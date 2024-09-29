configFile := "config.ini"
IniRead, ProcessName, %configFile%, Settings, ProcessName
IniRead, ProcessPath, %configFile%, Settings, ProcessPath

Process, Exist, %ProcessName%
If Not ErrorLevel ; errorlevel will = 0 if process doesn't exist
	Run, %ProcessPath%
else
    WinActivate, SpeedCrunch
