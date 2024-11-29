from .base_controller import BaseController

class NetworkController(BaseController):
    def list_networks(self):
        """List available Wi-Fi networks."""
        output = self.execute_check_command(["nmcli", "-t", "-f", "SSID", "dev", "wifi"], shell=True)
        return output.splitlines()

    def connect_to_network(self, ssid, password):
        """Connect to a Wi-Fi network."""
        self.execute_command(f"nmcli dev wifi connect '{ssid}' password '{password}'")

    def toggle_network_interface(self, interface, state):
        """Enable or disable a network interface."""

        action = 'connect' if state else 'disconnect'
        self.execute_command(f"nmcli dev {action} {interface}")

    def get_network_interfaces_full_info(self):
        result = self.execute_check_command(["nmcli", "device", "status"]).decode("utf-8")
        interfaces = []

        for line in result.splitlines()[1:]: # skip header line
            interface_details = line.split()

            device_info = {
                "name": interface_details[0],
                "type": interface_details[1],
                "state": interface_details[2],
                "connection": interface_details[3],
            }

            interfaces.append(device_info)

        return interfaces

    def get_list_wifi(self):
        result = self.execute_check_command(["nmcli", "device", "wifi", "list"], shell=True)
        ssids = []

        for line in result.splitlines()[1:]:
            ssid = line.split()[0]
            ssids.append(ssid)

        return ssids

    def connect_wifi(self, ssid, password):
        """Connect to a Wi-Fi network."""
        self.execute_command(f"nmcli dev wifi connect '{ssid}' password '{password}'")

        return f"Connected to {ssid}"
