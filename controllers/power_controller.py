from .base_controller import BaseController
import os

class PowerController(BaseController):

    def shutdown(self):
        """Shut down the system."""
        self.execute_command("shutdown now")

    def reboot(self):
        """Reboot the system."""
        self.execute_command("reboot")

    def suspend(self):
        """Suspend the system."""
        self.execute_command("systemctl suspend")

    def logout(self):
        """Logout the system."""
        self.execute_command("systemctl logout")

    def refresh_battery_info(self):
        # try:
        #     # Read battery information from system files
        #     with open("/sys/class/power_supply/BAT0/capacity", "r") as f:
        #         percentage = f.read().strip()
        #
        #     with open("/sys/class/power_supply/BAT0/status", "r") as f:
        #         status = f.read().strip()
        #
        #     return status, percentage
        # except FileNotFoundError:
        #     return "No battery detected", "N/A"

        battery_path = "/sys/class/power_supply/BAT0/"
        if os.path.exists(battery_path):
            try:
                # Read all files in the battery directory
                info = []
                for file_name in os.listdir(battery_path):
                    file_path = os.path.join(battery_path, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, "r") as file:
                            value = file.read().strip()
                            info.append(f"{file_name}: {value}")

                # Update the text display
                return info
            except Exception as e:
                print(e)
        else:
            return []