from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSlider, QComboBox, QFrame, QTextEdit

from controllers.audio_controller import AudioController


class AudioTab(QWidget):
    def __init__(self):
        super().__init__()

        # self.volume_slider = None
        # self.volume_label = None
        # self.audio_output_combo = None
        # self.mute_button = None
        self.is_muted = False

        self.audio_controller = AudioController()

        self.init_ui()

        device = self.get_selected_device()
        self.set_device_info(device)


    def init_ui(self):
        layout = QVBoxLayout()

        volume_frame = self.init_volume_control_ui()
        layout.addWidget(volume_frame)

        device_info_frame = self.init_current_device_info_ui()
        layout.addWidget(device_info_frame)

        # Stretch to fill space
        layout.addStretch()

        self.mute_button.clicked.connect(self.toggle_mute)
        self.volume_slider.valueChanged.connect(self.change_volume)
        # Set Layout
        self.setLayout(layout)

    def init_volume_control_ui(self):

        volume_frame = QFrame()
        volume_frame.setFrameShape(QFrame.Shape.StyledPanel)
        volume_frame.setFrameShadow(QFrame.Shadow.Raised)

        volume_layout = QVBoxLayout()

        monitor_title = QLabel("Volume settings:")
        monitor_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 16px;")
        volume_layout.addWidget(monitor_title)

        # Audio Output
        self.audio_output_combo = QComboBox()
        self.audio_output_combo.addItems(self.get_audio_outputs())
        volume_layout.addWidget(QLabel("Audio Output:"))
        volume_layout.addWidget(self.audio_output_combo)

        # Volume
        self.volume_label = QLabel(f"Volume: {self.get_current_volume()}")

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(self.get_current_volume())
        self.volume_slider.setTickInterval(5)
        self.volume_slider.setSingleStep(5)
        self.volume_slider.setPageStep(5)
        self.volume_slider.setTickPosition(QSlider.TickPosition.TicksBelow)

        volume_layout.addWidget(self.volume_label)
        volume_layout.addWidget(self.volume_slider)

        # Mute Button
        self.mute_button = QPushButton("Mute/Unmute")
        volume_layout.addWidget(self.mute_button)

        volume_frame.setLayout(volume_layout)

        self.audio_output_combo.currentTextChanged.connect(self.refresh_audio_output)

        return volume_frame

    def init_current_device_info_ui(self):
        device_info_frame = QFrame()
        device_info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        device_info_frame.setFrameShadow(QFrame.Shadow.Raised)

        device_info_layout = QVBoxLayout()

        device_info_title = QLabel("Device info:")
        device_info_title.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 16px;")
        device_info_layout.addWidget(device_info_title)

        self.info_text = QTextEdit()
        self.info_text.setReadOnly(True)
        device_info_layout.addWidget(self.info_text)

        device_info_frame.setLayout(device_info_layout)

        return device_info_frame

    def refresh_audio_output(self):
        selected_device = self.get_selected_device()

        current_device_info = self.get_device_info(selected_device)
        if current_device_info is None:
            return
        current_volume = current_device_info["volume"]

        # current_volume = self.get_current_volume()
        self.volume_slider.setValue(current_volume)

        self.set_device_info(selected_device, current_device_info)

    def get_current_device_info(self):
        output_devices = self.audio_controller.list_audio_outputs_full()

        for device in output_devices:
            if device["status"] == "RUNNING":
                return device
        return None

    def get_device_info(self, device: str):
        output_devices = self.audio_controller.list_audio_outputs_full()

        for d in output_devices:
            if d["name"] == device:
                return d
        return None

    def get_default_sink(self):
        return self.audio_controller.get_default_sink()

    def get_current_volume(self):
        device = self.get_selected_device()

        return self.audio_controller.get_volume(device)

    def change_volume(self, value):
        device = self.get_selected_device()

        if value is None:
            value = self.volume_slider.value()

        self.volume_label.setText(f"Volume: {value}%")
        self.audio_controller.set_volume(device, value)

    def toggle_mute(self):
        self.is_muted = not self.is_muted
        self.volume_slider.setDisabled(self.is_muted)

        device = self.get_selected_device()
        self.audio_controller.toggle_mute(device)

    def get_selected_device(self):
        device = self.audio_output_combo.currentText()

        if device == "No device found":
            raise ValueError("No audio output device found")

        return device

    def get_audio_outputs(self):
        return self.audio_controller.list_audio_outputs()

    def set_device_info(self, device: str, current_device_info: dict = None):
        if current_device_info is None:
            current_device_info = self.get_device_info(device)

        info_str = "\n".join(f"{key}: {value}" for key, value in current_device_info.items())
        self.info_text.setText(info_str)
