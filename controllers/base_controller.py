import subprocess


class BaseController:
    def execute_command(self, command):
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    def execute_check_command(self, command: list[str], shell=False, universal_newlines=False) -> str:
        try:
            if not command:
                raise ValueError("Command must has arguments")
            result =  subprocess.check_output(command, shell=shell, universal_newlines=universal_newlines)
            if shell:
                return result.decode().strip()
            return result.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
