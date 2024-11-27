import subprocess

from .base_controller import BaseController

class AudioController(BaseController):
    def get_volume(self, device: str):
        if device is None:
            device = "@DEFAULT_SINK@"

        output = self.execute_check_command(["pactl", "get-sink-volume", device], universal_newlines=True)

        for line in output.splitlines():
            if "Volume:" in line:
                volume_percentage = line.split()[4]
                return int(volume_percentage.strip('%'))

    def set_volume(self, device: str, value: int):
        if device is None:
            device = "@DEFAULT_SINK@"
        self.execute_command(f"pactl set-sink-volume {device} {value}%")

    def toggle_mute(self, device: str):
        if device is None:
            device = "@DEFAULT_SINK@"
        self.execute_command(f"pactl set-sink-mute {device} toggle")

    def list_audio_outputs(self):
        command = ["pactl", "list", "sinks", "short"]

        result = self.execute_check_command(command, universal_newlines=True)
        output_devices = result.splitlines()

        return [line.split("\t")[1] for line in output_devices]

    def list_audio_outputs_full(self):
        command = ["pactl", "list", "sinks"]
        output_device_infos = self.execute_check_command(command, universal_newlines=True).splitlines()

        list_outputs = []
        device_info = {}
        for output_device_info in output_device_infos:
            items = output_device_info.split("\t")
            for item in items:
                if "Name:" in item:
                    # Reset for the new device
                    device_info['name'] = item.split(":")[1].strip()
                elif "State:" in item:
                    device_info['status'] = item.split(":")[1].strip()
                elif "Mute:" in item:
                    device_info['mute'] = item.split(":")[1].strip()
                elif "Volume:" in item and "front-left" in item:
                    volume_split = item.split("/")
                    volume_left = int(volume_split[1].strip().replace("%", ""))
                    volume_right = int(volume_split[3].strip().replace("%", ""))

                    device_info['volume_left'] = volume_left
                    device_info['volume_right'] = volume_right

                    device_info['volume'] = (int(volume_left) + int(volume_right)) // 2
                elif "Description:" in item:
                    device_info['description'] = item.split(":")[1].strip()
            list_outputs.append(device_info)

        return list_outputs

    def get_default_sink(self):
        """
        Get the name of the default sink (audio output device).
        :return: Default sink name as a string or None if not found.
        """
        try:
            output = self.execute_check_command(["pactl", "get-default-sink"])
            return output.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error getting default sink: {e}")
            return None