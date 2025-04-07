
# Run As Method: Elevated User Access in windows
```bat
set dir_path=\"C:\Users\santo\Some Notes\quick_notes\"
set application_path=C:\Users\santo\AppData\Local\Programs\Microsoft VS Code\Code.exe

@REM Launching VS Code within the project dir_path with elevated access with networks creds
C:\Windows\system32\runas.exe /netonly /user:USERS/santo "%application_path% %dir_path%"

```
Let's break down this `.bat` file command by command:

**Line 1: `set dir_path=\"C:\Users\santo\Some Notes\quick_notes\"`**

* **`set`**: This is a fundamental command in batch scripting used to define or modify environment variables.
* **`dir_path`**: This is the name you are assigning to the environment variable. You can choose almost any name.
* **`=`**: This is the assignment operator, linking the variable name to its value.
* **`\"C:\Users\santo\Some Notes\quick_notes\"`**: This is the value being assigned to the `dir_path` variable.
    * Notice the double quotes (`\"`). In batch files, double quotes are often used to enclose paths that contain spaces. The backslashes (`\`) before the double quotes are used to escape them, so they are treated as literal double quote characters within the string.
    * This path likely points to a directory on your computer where you store your "quick notes".

**In essence, this line creates an environment variable named `dir_path` and stores the path `C:\Users\santo\Some Notes\quick_notes` in it.**

**Line 2: `set application_path=C:\Users\santo\AppData\Local\Programs\Microsoft VS Code\Code.exe`**

* **`set`**: Again, the command to define an environment variable.
* **`application_path`**: This is the name of the environment variable.
* **`=`**: The assignment operator.
* **`C:\Users\santo\AppData\Local\Programs\Microsoft VS Code\Code.exe`**: This is the path to the executable file for Microsoft Visual Studio Code (VS Code).

**This line creates an environment variable named `application_path` and stores the path to the VS Code executable in it.**

**Line 4: `@REM Launching VS Code within the project dir_path with elevated access with networks creds`**

* **`@`**: This symbol at the beginning of the line suppresses the command itself from being displayed in the command prompt when the script runs. Only the output of the command will be shown.
* **`REM`**: This stands for "Remark". It's used to add comments to your batch file. Anything after `REM` on the same line is ignored by the command interpreter.
* **`Launching VS Code within the project dir_path with elevated access with networks creds`**: This is a comment explaining the purpose of the following command. However, the comment isn't entirely accurate regarding "elevated access".

**This line is a comment explaining what the next command intends to do.**

**Line 5: `C:\Windows\system32\runas.exe /netonly /user:USERS/santo "%application_path% %dir_path%"`**

* **`C:\Windows\system32\runas.exe`**: This is a built-in Windows command-line utility that allows you to run programs as a different user.
* **`/netonly`**: This switch specifies that the user account provided will only be used for accessing remote resources (like network shares). The program itself will run with the current user's credentials on the local machine. **This does NOT provide elevated (administrator) access.**
* **`/user:USERS/santo`**: This specifies the user account under which the program should be run for network access.
    * `USERS` is likely the name of your computer or a domain.
    * `santo` is the username.
    * So, this tells `runas` to use the network credentials of the user named "santo" on the machine/domain "USERS".
* **`"%application_path% %dir_path%"`**: These are the arguments being passed to the `Code.exe` application.
    * `%application_path%`: This will be replaced by the value stored in the `application_path` environment variable (the path to `Code.exe`).
    * `%dir_path%`: This will be replaced by the value stored in the `dir_path` environment variable (the path to your "quick_notes" directory).
    * The spaces between `%application_path%` and `%dir_path%` will be treated as separators between command-line arguments for VS Code. VS Code will likely interpret the directory path as the folder to open upon launch.

**In summary, this line attempts to launch Microsoft VS Code using the network credentials of the user `USERS\santo` while running the application itself with the current user's local permissions. It also passes the `dir_path` as a command-line argument to VS Code, likely instructing it to open that directory.**

**Important Considerations:**

* **Password Prompt:** When this command is executed, you will likely be prompted to enter the password for the `USERS\santo` user account.
* **"Elevated Access":** The comment is misleading. The `/netonly` switch specifically avoids running the application with the specified user's full credentials (which could include elevated privileges). It only uses those credentials for network authentication. To run VS Code with administrator privileges, you would typically use the `/trustlevel:highest` switch (though this might not be compatible with `/netonly`).
* **Network Credentials:** This script assumes that the `USERS\santo` user has the necessary permissions to access any network resources VS Code might need.
* **Local Permissions:** VS Code itself will run with the permissions of the user who executes this `.bat` file on their local machine.


