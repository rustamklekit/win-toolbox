; Dismisses extension rename warning
; Auto dismiss file extension change dialog in Windows Explorer when renaming

SetTitleMatchMode 3
SetControlDelay -1

while true {
    if WinActive("Rename ahk_class #32770 ahk_exe explorer.exe") { ; faster response than WinWaitActive & same CPU usage
        SoundBeep(0, 0) ; Cut off notification sound by playing silence
        ControlClick("Button1")
        WinWaitNotActive()
    }
    Sleep(15)
}
