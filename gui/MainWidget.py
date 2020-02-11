from PyQt5 import QtWidgets

from gui.recordVideo import RecordVideo
from src.VideoBehavior import VideoBehavior


class MainWidget(QtWidgets.QWidget):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.videoBehavior = VideoBehavior()
                # TODO: set video port
                self.record_video = RecordVideo(0)
                self.run_button = QtWidgets.QPushButton('Start')

                # Connect the image data signal and slot together
                image_data_slot = self.videoBehavior.image_data_slot
                self.record_video.image_data.connect(image_data_slot)
                # connect the run button to the start recording slot
                self.run_button.clicked.connect(self.record_video.start_recording)

                # Create and set the layout
                layout = QtWidgets.QVBoxLayout()
                layout.addWidget(self.videoBehavior)
                layout.addWidget(self.run_button)

                self.setLayout(layout)