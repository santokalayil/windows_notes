import os
import subprocess
from typing import Optional, List, Tuple

def run_application_with_runas(
    application_path: str,
    dir_path: str,
    username: str,
    password: Optional[str] = None,
) -> bool:
    """
    Launches an application (like VS Code) with 'runas.exe' to use different credentials.

    This function attempts to replicate the behavior of the original batch script,
    using 'runas.exe' to launch the application with the specified username.
    It includes an option for providing a password, but this is NOT recommended
    for security reasons.

    Args:
        application_path (str): The path to the application's executable.
        dir_path (str): The path to the directory to open.
        username (str): The username to use with 'runas.exe' (e.g., "DOMAIN\user").
        password (Optional[str], optional): The password for the specified user.
            Providing the password directly is insecure and should be avoided if
            possible. If None, the user will be prompted to enter the password.

    Returns:
        bool: True if the application was launched successfully, False otherwise.
    """
    try:
        # Construct the 'runas' command.
        command: List[str] = [
            "C:\\Windows\\System32\\runas.exe",
            "/netonly",  # Use network credentials only.
            f"/user:{username}",
            application_path,
            dir_path,
        ]

        print(f"Attempting to launch: {application_path} with runas as {username} and directory: {dir_path}")

        process: subprocess.Popen
        if password:
            # **SECURITY WARNING:** Passing the password directly is insecure!
            # It can expose the password in the script itself or in command history.
            #  subprocess.run can take input
            process = subprocess.Popen(command, stdin=subprocess.PIPE, text=True)
            process.communicate(input=password + "\n")  # Add newline for the password prompt
        else:
            # If no password is provided, the user will be prompted to enter it.
            process = subprocess.Popen(command)
            process.wait()  # wait for the process to complete

        if process.returncode == 0:
            print("Application launched successfully.")
            return True
        else:
            print(f"Application launch failed with return code: {process.returncode}")
            return False

    except FileNotFoundError:
        print("Error: 'runas.exe' not found or application not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False



def main() -> None:
    """
    Main function to define paths, username, and launch the application using runas.
    """
    # Define the directory path.
    dir_path: str = r"C:\Users\santo\Some Notes\quick_notes"
    # Define the application path.
    application_path: str = r"C:\Users\santo\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    # Define the username for 'runas.exe'.  **Replace this with your actual username!**
    username: str = "USERS\\santo"  # <--------  CHANGE THIS!!!

    # Launch the application using runas.  Provide the password here ONLY if you
    # understand the security implications.  It's generally better to omit it
    # and let the user enter it at the prompt.
    # password = "your_password"  # <--------  AVOID THIS IF POSSIBLE!
    password: Optional[str] = None  # Best Practice: Prompt the user for the password.

    if run_application_with_runas(application_path, dir_path, username, password):
        print("Application launch was initiated.")
    else:
        print("Application launch was not successful.")



if __name__ == "__main__":
    main()
