import subprocess
from .base_controller import BaseController


class DisplayController(BaseController):
    def get_displays(self):
        """Detect connected displays using xrandr."""
        output = subprocess.check_output("xrandr --listmonitors", shell=True)
        displays = [line.split()[3] for line in output.decode().splitlines() if "+" in line]
        return displays

    def get_resolutions(self, display):
        """Get available resolutions for a given display."""
        output = subprocess.check_output(f"xrandr --query | grep '{display}' -A10", shell=True)
        resolutions = [
            line.split()[0] for line in output.decode().splitlines()[1:] if "x" in line
        ]
        return resolutions

    def set_resolution(self, display, resolution):
        """Set resolution for a specific display."""
        self.execute_command(f"xrandr --output {display} --mode {resolution}")

    def get_brightness(self):
        current_brightness = self.execute_check_command(["brightnessctl", "get"])
        max_brightness = self.execute_check_command(["brightnessctl", "max"])

        current = int(current_brightness)
        maximum = int(max_brightness)
        percentage = int((current / maximum) * 100)
        return percentage

    def set_brightness(self, value):
        """Set brightness for a specific display."""
        print("setting brightness: {value}".format(value=value))

        self.execute_command(f"brightnessctl set {value}%")