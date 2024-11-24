from .base_controller import BaseController

class NetworkController(BaseController):
    def list_networks(self):
        """List available Wi-Fi networks."""
        import subprocess
        output = subprocess.check_output("nmcli -t -f SSID dev wifi", shell=True)
        return output.decode().splitlines()

    def connect_to_network(self, ssid, password):
        """Connect to a Wi-Fi network."""
        self.execute_command(f"nmcli dev wifi connect '{ssid}' password '{password}'")

    def toggle_network_interface(self, interface, state):
        """Enable or disable a network interface."""
        self.execute_command(f"nmcli dev set {interface} {'up' if state else 'down'}")
