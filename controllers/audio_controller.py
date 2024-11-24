from .base_controller import BaseController

class AudioController(BaseController):
    def get_volume(self):
        self.execute_command(f"")

    def set_volume(self, value):
        self.execute_command(f"pactl set-sink-volume @DEFAULT_SINK@ {value}%")

    def toggle_mute(self):
        self.execute_command("pactl set-sink-mute @DEFAULT_SINK@ toggle")

    def list_audio_outputs(self):
        import subprocess
        result = subprocess.check_output("pactl list sinks short", shell=True)
        output_devices = result.decode().splitlines()
        return [line.split("\t")[1] for line in output_devices]