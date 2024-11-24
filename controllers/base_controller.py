import subprocess


class BaseController:
    def execute_command(self, command):
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    def execute_check_command(self, command: list[str]):
        try:
            if len(command) != 2:
                raise ValueError("Command must have 2 arguments")
            return subprocess.check_output([command[0], command[1]]).decode().strip()
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
