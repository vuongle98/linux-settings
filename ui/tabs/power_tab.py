from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit

from controllers.power_controller import PowerController


class PowerTab(QWidget):
    def __init__(self):
        super().__init__()

        self.power_controller = PowerController()
        self.init_ui()
        self.refresh_battery_info()

        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_battery_info)
        self.timer.start(5000)  # Refresh every 5 seconds

    def init_ui(self):
        layout = QVBoxLayout()

        # Battery info display
        self.battery_info_display = QTextEdit()
        self.battery_info_display.setReadOnly(True)
        layout.addWidget(self.battery_info_display)

        # Refresh button
        refresh_button = QPushButton("Refresh Battery Info")
        layout.addWidget(refresh_button)

        refresh_button.clicked.connect(self.refresh_battery_info)

        # Power buttons
        self.shutdown_button = QPushButton("Shutdown")
        self.reboot_button = QPushButton("Reboot")
        self.suspend_button = QPushButton("Suspend")
        self.logout_button = QPushButton("Logout")

        layout.addWidget(self.logout_button)
        layout.addWidget(self.shutdown_button)
        layout.addWidget(self.reboot_button)
        layout.addWidget(self.suspend_button)

        # Set layout
        self.setLayout(layout)

        # Connect buttons (actions are placeholders)
        self.shutdown_button.clicked.connect(self.shutdown)
        self.reboot_button.clicked.connect(self.reboot)
        self.suspend_button.clicked.connect(self.suspend)
        self.logout_button.clicked.connect(self.logout)

    def shutdown(self):
        self.power_controller.shutdown()

    def reboot(self):
        self.power_controller.reboot()

    def logout(self):
        self.power_controller.logout()

    def suspend(self):
        self.power_controller.suspend()

    def refresh_battery_info(self):
        info = self.power_controller.refresh_battery_info()
        info_str = "\n".join(info)
        self.battery_info_display.setPlainText(info_str)