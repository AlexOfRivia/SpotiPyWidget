import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout,QWidget

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("My Compiled App")

        #album cover

        #song labels
        song_title_label = QLabel("Homecoming")
        artist_label = QLabel("Kanye West")

        




        #main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(label)
        main_layout.addWidget(button)

        self.setLayout(main_layout)
    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()