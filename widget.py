import sys
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout ,QWidget
from PyQt6.QtCore import QTimer
from dotenv import load_dotenv

class MainWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("My Compiled App")
        load_dotenv()
        
        client_id = os.environ.get("CLIENT_ID")
        client_secret = os.environ.get("CLIENT_SECRET")
        scope = "user-read-private user-modify-playback-state user-read-playback-state"


        auth_manager = SpotifyOAuth(client_secret=client_secret, client_id=client_id,redirect_uri="http://127.0.0.1:9090",scope=scope)
        self.sp = spotipy.Spotify(auth_manager=auth_manager)

        #album cover


        #song labels
        self.song_title_label = QLabel("")
        self.artist_label = QLabel("")

        song_layout = QVBoxLayout()
        song_layout.addWidget(self.song_title_label)
        song_layout.addWidget(self.artist_label)

        #buttons
        prev_button = QPushButton(
            text="Prev"
        )

        prev_button.setFixedSize(50,20)

        prev_button.pressed.connect(self.prev_track)

        play_pause_button = QPushButton(
            text="Play/Pause"
        )

        play_pause_button.setFixedSize(75,20)
        play_pause_button.pressed.connect(self.play_pause_track)


        next_button = QPushButton(
            text="Next"
        )

        next_button.pressed.connect(self.skip_track)

        next_button.setFixedSize(50,20)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(prev_button)
        buttons_layout.addWidget(play_pause_button)
        buttons_layout.addWidget(next_button)

        #main layout
        main_layout = QVBoxLayout()

        main_layout.addLayout(song_layout)
        main_layout.addLayout(buttons_layout)

        self.fetch_current_song()
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_current_song)
        self.timer.start(3000)  #wait for 5 seconds


        self.setLayout(main_layout)

    def prev_track(self):
        self.sp.previous_track()

    def skip_track(self):
        self.sp.next_track()

    def play_pause_track(self):
        #prolly gonna use is_playing from the current track 
        self.sp.pause_playback()

    def fetch_current_song(self):
        try:
            track = self.sp.current_user_playing_track(market=None, additional_types=('track',))
        except Exception as e:
            print(f"Errot: {e}")
            track = None

        if track is None or track['item'] is None:
            song_title = ''
            artist = ''
        else:
            song_title = track['item']['name']
            artist = track['item']['artists'][0]['name']
        self.song_title_label.setText(song_title)
        self.artist_label.setText(artist)

            
    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()