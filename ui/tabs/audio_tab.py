from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSlider, QComboBox

from controllers.audio_controller import AudioController


class AudioTab(QWidget):
    def __init__(self):
        super().__init__()

        self.audio_controller = AudioController()

        self.init_ui()


    def init_ui(self):
        layout = QVBoxLayout()

        # Volume
        self.volume_label = QLabel("Volume: 50%", self)
        layout.addWidget(self.volume_label)
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.change_volume)
        layout.addWidget(self.volume_slider)

        # Mute Button
        self.mute_button = QPushButton("Mute/Unmute")
        self.mute_button.clicked.connect(self.toggle_mute)
        layout.addWidget(self.mute_button)

        # Audio Output
        self.audio_output_combo = QComboBox()
        self.audio_output_combo.addItems(self.get_audio_outputs())
        layout.addWidget(QLabel("Audio Output:"))
        layout.addWidget(self.audio_output_combo)

        # Stretch to fill space
        layout.addStretch()

        # Set Layout
        self.setLayout(layout)

    def change_volume(self, value):
        self.volume_label.setText(f"Volume: {value}%")
        self.audio_controller.set_volume(value)

    def toggle_mute(self):
        self.audio_controller.toggle_mute()

    def get_audio_outputs(self):
        return self.audio_controller.list_audio_outputs()
