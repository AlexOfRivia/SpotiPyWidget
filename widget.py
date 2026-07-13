import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout ,QWidget

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("My Compiled App")

        #album cover


        #song labels
        song_title_label = QLabel("Homecoming")
        artist_label = QLabel("Kanye West")

        song_layout = QVBoxLayout()
        song_layout.addWidget(song_title_label)
        song_layout.addWidget(artist_label)

        #buttons
        prev_button = QPushButton(
            text="Prev"
        )

        prev_button.setFixedSize(50,20)

        play_pause_button = QPushButton(
            text="Play/Pause"
        )

        play_pause_button.setFixedSize(75,20)

        next_button = QPushButton(
            text="Next"
        )

        next_button.setFixedSize(50,20)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(prev_button)
        buttons_layout.addWidget(play_pause_button)
        buttons_layout.addWidget(next_button)

        #main layout
        main_layout = QVBoxLayout()

        main_layout.addLayout(song_layout)
        main_layout.addLayout(buttons_layout)


        self.setLayout(main_layout)
    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()