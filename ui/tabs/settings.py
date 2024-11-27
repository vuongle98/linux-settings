from PyQt6.QtWidgets import QWidget, QComboBox, QVBoxLayout, QApplication


class SettingsTab(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Theme ComboBox
        theme_combo = QComboBox()
        theme_combo.addItems(["Default", "Dark", "System"])
        theme_combo.currentTextChanged.connect(self.switch_theme)
        layout.addWidget(theme_combo)

        self.setLayout(layout)

    def switch_theme(self, theme: str):
        if theme == "Default":
            self.setStyleSheet("")
        elif theme == "Dark":
            self.set_dark_theme()
        elif theme == "System":
            self.apply_system_theme()

    def set_dark_theme(self):
        pass

    def apply_system_theme(self):
        # For simplicity, let's use the Default style as an example for "System"
        pass