import sys
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout ,QWidget
from dotenv import load_dotenv

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("My Compiled App")

        load_dotenv()

        playback_flag = 0   #0 not playing, 1 playing

        client_id = os.environ.get("CLIENT_ID")
        client_secret = os.environ.get("CLIENT_SECRET")
        scope = "user-read-private user-modify-playback-state user-read-playback-state"

        auth_manager = SpotifyOAuth(client_secret=client_secret, client_id=client_id,redirect_uri="http://127.0.0.1:9090",scope=scope)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        user = sp.current_user()
        print(user)

        

        #loading variables, if nothing is playing, then will set to empty 


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