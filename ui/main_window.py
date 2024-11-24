from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton, QTabWidget, QShortcut
)
from ui.tabs.audio_tab import AudioTab
from ui.tabs.display_tab import DisplayTab
from ui.tabs.network_tab import NetworkTab
from ui.tabs.power_tab import PowerTab
from ui.tabs.user_management_tab import UserManagementTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linux Display & Audio Control")
        self.setGeometry(100, 100, 500, 400)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.tabs = QTabWidget(self)
        layout.addWidget(self.tabs)

        # Add Exit Button
        self.exit_button = QPushButton("Exit")
        layout.addWidget(self.exit_button)

        # Connect Exit Button to Quit Application
        self.exit_button.clicked.connect(self.close_application)

        self.tabs.addTab(PowerTab(), "Power")
        self.tabs.addTab(DisplayTab(), "Display")
        self.tabs.addTab(AudioTab(), "Audio")
        self.tabs.addTab(NetworkTab(), "Network")
        self.tabs.addTab(UserManagementTab(), "User Management")

        # Exit app when press shortcut Ctrl + Q
        self.exit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.exit_shortcut.activated.connect(self.close_application)

        self.setCentralWidget(central_widget)

    def close_application(self):
        self.close()