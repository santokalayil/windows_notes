
# Run As Method: Elevated User Access in windows
```bat
set dir_path=\"C:\Users\santo\Some Notes\quick_notes\"
set application_path=C:\Users\santo\AppData\Local\Programs\Microsoft VS Code\Code.exe

@REM Launching VS Code within the project dir_path with elevated access with networks creds
C:\Windows\system32\runas.exe /netonly /user:USERS/santo "%application_path% %dir_path%"

```

