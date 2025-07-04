import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QComboBox, QMessageBox
import subprocess

class WorldClassTweaks(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Class Tweaks")
        self.setGeometry(200, 200, 500, 400)

        self.label = QLabel("Choose a tweak category:")
        self.combo = QComboBox()
        self.combo.addItems([
            "FPS Boost",
            "Low Ping",
            "Input Delay",
            "Power Tweaks",
            "Game Specific (Fortnite, Roblox)",
            "Anti-Cheat Safe",
            "BIOS Tips",
            "Auto Tuner",
            "AI Smart Presets",
            "Run All Tweaks"
        ])

        self.button = QPushButton("Apply Selected Tweaks")
        self.button.clicked.connect(self.apply_tweaks)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def apply_tweaks(self):
        choice = self.combo.currentText()

        script_map = {
            "FPS Boost": "scripts/FPS/run_fps.cmd",
            "Low Ping": "scripts/Ping/run_ping.cmd",
            "Input Delay": "scripts/Input/run_input.cmd",
            "Power Tweaks": "scripts/Power/run_power.cmd",
            "Game Specific (Fortnite, Roblox)": "scripts/GameSpecific/run_games.cmd",
            "Anti-Cheat Safe": "scripts/AntiCheatSafe/run_anticheat.cmd",
            "BIOS Tips": "scripts/BIOS/run_bios.cmd",
            "Auto Tuner": "scripts/AutoTuner/auto_tuner.cmd",
            "AI Smart Presets": "scripts/AI/smart_presets.cmd",
            "Run All Tweaks": "scripts/RunAll/run_all.cmd"
        }

        script = script_map.get(choice)
        if script and os.path.exists(script):
            subprocess.call(script, shell=True)
        else:
            QMessageBox.warning(self, "Error", f"Script not found:\n{script}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorldClassTweaks()
    window.show()
    sys.exit(app.exec())
