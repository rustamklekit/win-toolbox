; This script changes JAVA_HOME environmental variable with the path to java version a user desires.
; In order to use this script intended java version should be installed and path should be set in environmental variable JAVA_HOME_X, with X is java version.
; examples:
; to set to java 8 : set_java.ahk 8
; to set from user input run without arguments

; Get java version from a command-line argument; If no argument provided - ask for a user input.
JavaVersionToSet := A_Args.Length > 0 ? JavaVersionToSet := A_Args[1] :  InputBox("Please, enter a Java version", "Enter Java Version").value

JavaHomeEnvVariable := "JAVA_HOME"

JavaVersionEnvVariable := "JAVA_HOME_" . JavaVersionToSet
VersionPath := EnvGet(JavaVersionEnvVariable)
if (VersionPath) {
    RegWrite VersionPath, "REG_EXPAND_SZ", "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment", JavaHomeEnvVariable
} else {
    MsgBox "Error: JAVA_HOME_" . JavaVersionToSet . " is not found in environment variables."
}


