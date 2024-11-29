from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QLabel, QComboBox, QTextEdit, QPushButton

from controllers.network_controller import NetworkController


class NetworkTab(QWidget):
    def __init__(self):
        super().__init__()

        self.network_controller = NetworkController()
        self.init_ui()

        device = self.network_combo.currentText()
        self.set_info(device)

    def init_ui(self):
        network_layout = QVBoxLayout()

        network_control_frame = self.init_network_control_ui()
        network_layout.addWidget(network_control_frame)

        network_info_frame = self.init_network_info_ui()
        network_layout.addWidget(network_info_frame)
        # add stretch
        network_layout.addStretch()

        # Set Layout
        self.setLayout(network_layout)

    def init_network_control_ui(self):
        network_control_frame = QFrame()
        network_control_frame.setFrameShape(QFrame.Shape.StyledPanel)
        network_control_frame.setFrameShadow(QFrame.Shadow.Raised)

        network_control_layout = QVBoxLayout()
        network_control_title = QLabel("Network controls:")
        network_control_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 16px;")
        network_control_layout.addWidget(network_control_title)

        self.network_combo = QComboBox()
        network_interfaces_full_info = self.network_controller.get_network_interfaces_full_info()
        self.network_combo.addItems([item["name"] for item in network_interfaces_full_info])
        self.network_combo.currentTextChanged.connect(self.load_network_info)

        network_control_layout.addWidget(self.network_combo)

        self.toggle_button = QPushButton("Enable/Disable Interface")
        self.toggle_button.clicked.connect(self.toggle_network_state)
        network_control_layout.addWidget(self.toggle_button)

        network_control_frame.setLayout(network_control_layout)

        return network_control_frame

    def init_network_info_ui(self):
        network_info_frame = QFrame()
        network_info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        network_info_frame.setFrameShadow(QFrame.Shadow.Raised)

        network_info_layout = QVBoxLayout()
        network_info_title = QLabel("Network info:")
        network_info_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 16px;")
        network_info_layout.addWidget(network_info_title)

        self.device_info_text = QTextEdit()
        self.device_info_text.setReadOnly(True)
        network_info_layout.addWidget(self.device_info_text)

        network_info_frame.setLayout(network_info_layout)

        return network_info_frame

    def toggle_network_state(self):
        device = self.network_combo.currentText()

        enable = self.toggle_button.text() == "Enable Interface"
        self.network_controller.toggle_network_interface(device, enable)
        self.toggle_button.setText("Disable Interface" if enable else "Enable Interface")
        self.set_info(device)

    def load_network_info(self, device: str):
        network_infos = self.network_controller.get_network_interfaces_full_info()
        self.set_info(device, network_infos)

    def set_info(self, device: str, network_infos: list[dict] = None):
        if network_infos is None:
            network_infos = self.network_controller.get_network_interfaces_full_info()

        for network_info in network_infos:
            if network_info["name"] == device:
                info = "\n".join(f"{key}: {value}" for key, value in network_info.items())
                self.device_info_text.setText(info)