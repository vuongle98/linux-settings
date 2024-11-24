from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QSlider, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt

from controllers.display_controller import DisplayController


class DisplayTab(QWidget):
    def __init__(self):
        super().__init__()

        self.display_controller = DisplayController()


        self.displays = self.get_displays()
        self.current_display = self.displays[0]

        self.init_ui()


    def init_ui(self):
        layout = QVBoxLayout()

        # Screen Resolution Section
        display_layout = QVBoxLayout()

        # Scan monitor
        self.monitor_button = QPushButton("Detect Monitors")
        display_layout.addWidget(self.monitor_button)

        # display
        self.display_dropdown = QComboBox()
        self.display_dropdown.addItems(self.displays)
        self.display_dropdown.currentTextChanged.connect(self.change_current_display)
        display_layout.addWidget(QLabel("Displays:"))
        display_layout.addWidget(self.display_dropdown)

        # Resolution
        self.resolution_dropdown = QComboBox()
        display_layout.addWidget(QLabel("Resolution:"))
        self.resolution_dropdown.addItems(self.get_resolution(self.current_display))
        self.resolution_dropdown.currentTextChanged.connect(self.apply_resolution_changes)
        display_layout.addWidget(self.resolution_dropdown)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Brightness Control Section
        self.brightness_label = QLabel("Brightness: 50%")
        self.brightness_slider = QSlider(Qt.Horizontal)
        self.brightness_slider.setRange(0, 100)
        self.brightness_slider.setMinimum(10)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setValue(self.get_brightness_level())
        self.brightness_slider.setTickInterval(10)
        self.brightness_slider.setSingleStep(10)
        self.brightness_slider.setPageStep(10)
        self.brightness_slider.setTickPosition(QSlider.TicksBelow)

        display_layout.addWidget(self.brightness_label)
        display_layout.addWidget(self.brightness_slider)
        display_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(display_layout)

        # Stretch to fill space
        layout.addStretch()

        # Set Layout
        self.setLayout(layout)

        # Connect Actions
        self.brightness_slider.valueChanged.connect(self.set_brightness)
        self.monitor_button.clicked.connect(self.refresh_displays)

    def get_displays(self):
        return self.display_controller.get_displays()

    def get_resolution(self, display):
        return self.display_controller.get_resolutions(self.current_display)

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
        self.display_controller.set_resolution(self.current_display, resolution)

    def change_current_display(self, display: str):
        self.current_display = display
        self.resolution_dropdown.clear()
        self.resolution_dropdown.addItems(self.get_resolution(self.current_display))
