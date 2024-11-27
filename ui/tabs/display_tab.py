from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QSlider, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QStyle,
    QGroupBox, QFrame
)
from PyQt6.QtCore import Qt

from controllers.display_controller import DisplayController


class DisplayTab(QWidget):
    def __init__(self):
        super().__init__()

        self.resolution_dropdown = None
        self.display_dropdown = None
        self.brightness_label = None
        self.display_controller = DisplayController()


        self.displays = self.get_displays()
        self.current_display = self.displays[0]

        self.init_ui()


    def init_ui(self):
        layout = QVBoxLayout()

        # Screen Resolution Section
        display_layout = QVBoxLayout()

        monitor_frame = self.init_monitor_settings_ui()
        display_layout.addWidget(monitor_frame)
        display_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        brightness_frame = self.init_brightness_settings_ui()
        display_layout.addWidget(brightness_frame)
        display_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(display_layout)

        # Stretch to fill space
        layout.addStretch()

        # Set Layout
        self.setLayout(layout)

    def init_brightness_settings_ui(self):
        brightness_layout = QVBoxLayout()
        brightness_title = QLabel("Brightness settings:")
        brightness_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 16px;")
        brightness_layout.addWidget(brightness_title)
        
        # Brightness Control Section
        self.brightness_label = QLabel("Brightness level: 50%")
        brightness_slider = QSlider(Qt.Orientation.Horizontal)
        brightness_slider.setRange(0, 100)
        brightness_slider.setMinimum(10)
        brightness_slider.setMaximum(100)
        brightness_slider.setValue(self.get_brightness_level())
        brightness_slider.setTickInterval(10)
        brightness_slider.setSingleStep(10)
        brightness_slider.setPageStep(10)
        brightness_slider.setTickPosition(QSlider.TickPosition.TicksBelow)

        brightness_frame = QFrame()
        brightness_frame.setFrameShape(QFrame.Shape.StyledPanel)
        brightness_frame.setFrameShadow(QFrame.Shadow.Raised)

        brightness_layout.addWidget(self.brightness_label)
        brightness_layout.addWidget(brightness_slider)

        brightness_frame.setLayout(brightness_layout)

        # Connect Actions
        brightness_slider.valueChanged.connect(self.set_brightness)

        return brightness_frame

    def init_monitor_settings_ui(self):
        monitor_frame = QFrame()
        monitor_frame.setFrameShape(QFrame.Shape.StyledPanel)
        monitor_frame.setFrameShadow(QFrame.Shadow.Raised)

        monitor_layout = QVBoxLayout()

        monitor_title = QLabel("Monitor settings:")
        monitor_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 16px;")
        monitor_layout.addWidget(monitor_title)

        # Scan monitor
        monitor_button = QPushButton("Detect Monitors")
        monitor_layout.addWidget(monitor_button)

        # Monitors
        self.display_dropdown = QComboBox()
        self.display_dropdown.addItems(self.displays)
        self.display_dropdown.currentTextChanged.connect(self.change_current_display)
        monitor_layout.addWidget(QLabel("Monitors:"))
        monitor_layout.addWidget(self.display_dropdown)

        # Resolution
        self.resolution_dropdown = QComboBox()
        monitor_layout.addWidget(QLabel("Resolution:"))
        self.resolution_dropdown.addItems(self.get_resolution(self.current_display))
        self.resolution_dropdown.currentTextChanged.connect(self.apply_resolution_changes)
        monitor_layout.addWidget(self.resolution_dropdown)

        monitor_frame.setLayout(monitor_layout)

        # Connect Actions
        monitor_button.clicked.connect(self.refresh_displays)

        return monitor_frame

    def get_displays(self):
        return self.display_controller.get_displays()

    def get_resolution(self, display):
        return self.display_controller.get_resolutions(display)

    def get_brightness_level(self):
        return self.display_controller.get_brightness()

    def set_brightness(self, value):
        """Update brightness label based on slider."""
        self.brightness_label.setText(f"Brightness: {value}%")
        # Add system-level code to adjust brightness here.
        self.display_controller.set_brightness(value)

    def refresh_displays(self):
        self.display_dropdown.clear()
        self.displays = self.get_displays()
        self.current_display = self.displays[0]

        self.display_dropdown.addItems(self.displays)

    def apply_resolution_changes(self, resolution: str):
        if resolution and self.current_display:
            self.display_controller.set_resolution(self.current_display, resolution)

    def change_current_display(self, display: str):
        self.current_display = display
        self.resolution_dropdown.clear()
        self.resolution_dropdown.addItems(self.get_resolution(self.current_display))
