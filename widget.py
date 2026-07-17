import sys
import os
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QTimer, Qt
from dotenv import load_dotenv

# TODO
# add more playback functionality

#stylesheets
button_stylesheet = """QPushButton{
        background-color: #1db954;
        color: #ffffff;
        border-radius: 10px;
        font-weight: bold;
        font-size: 12px;
}
QPushButton:hover { background-color: #21cc5d; }
QPushButton:pressed { background-color: #0a401d; }
"""

title_label_stylesheet = """
QLabel { 
    color: #ffffff;
    font-size: 16px;
    font-weight: semibold;
 }
"""

artist_label_stylesheet = """
QLabel { 
    color: #b3b3b3;
    font-size: 12px;
 }
"""


class MainWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("My Compiled App")
        self.setStyleSheet("background-color: #121212;")
        self.setFixedSize(250,275)
        load_dotenv()
        
        client_id = os.environ.get("CLIENT_ID")
        client_secret = os.environ.get("CLIENT_SECRET")
        scope = "user-read-private user-modify-playback-state user-read-playback-state"


        auth_manager = SpotifyOAuth(client_secret=client_secret, client_id=client_id,redirect_uri="http://127.0.0.1:9090",scope=scope)
        self.sp = spotipy.Spotify(auth_manager=auth_manager)

        #------------------------labels-------------------------

        #album cover
        self.album_cover_label = QLabel()
        

        #song labels
        self.song_title_label = QLabel("")
        self.song_title_label.setStyleSheet(title_label_stylesheet)

        self.artist_label = QLabel("")
        self.artist_label.setStyleSheet(artist_label_stylesheet)

        #-------------------------------------------------------



        #-----------------labels-layout-------------------------

        song_layout = QVBoxLayout()
        song_layout.addWidget(self.album_cover_label, alignment=Qt.AlignmentFlag.AlignCenter)
        song_layout.addWidget(self.song_title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        song_layout.addWidget(self.artist_label, alignment=Qt.AlignmentFlag.AlignCenter)

        #-------------------------------------------------------



        #----------------------buttons--------------------------

        prev_button = QPushButton(text="Prev")
        prev_button.setStyleSheet(button_stylesheet)
        

        prev_button.setFixedSize(50,25)
        prev_button.pressed.connect(self.prev_track)


        play_pause_button = QPushButton(text="Play/Pause")
        play_pause_button.setStyleSheet(button_stylesheet)

        play_pause_button.setFixedSize(75,25)
        play_pause_button.pressed.connect(self.play_pause_track)


        next_button = QPushButton(text="Next")
        next_button.setStyleSheet(button_stylesheet)

        next_button.pressed.connect(self.skip_track)
        next_button.setFixedSize(50,25)

        #-------------------------------------------------------


        
        #------------------buttons-layout-----------------------

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(prev_button)
        buttons_layout.addWidget(play_pause_button)
        buttons_layout.addWidget(next_button)

        #-------------------------------------------------------

        #main layout
        main_layout = QVBoxLayout()

        main_layout.addLayout(song_layout)
        main_layout.addLayout(buttons_layout)

        self.fetch_current_song()
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_current_song)
        self.timer.start(3000)  #wait for 3 seconds


        self.setLayout(main_layout)


    #------------------------methods----------------------------

    def prev_track(self):
        if self.sp.current_user_playing_track(market=None, additional_types=('track',)) is not None:
            self.sp.previous_track()

    def skip_track(self):
        if self.sp.current_user_playing_track(market=None, additional_types=('track',)) is not None:
            self.sp.next_track()

    def play_pause_track(self):
        #prolly gonna use is_playing from the current track 
        current_track = self.sp.current_user_playing_track(market=None, additional_types=('track',))
        
        if current_track is not None:
            try:
                if current_track['is_playing']:
                    self.sp.pause_playback()
                    return
                else:
                    self.sp.start_playback()
                    return
            except Exception as e:
                print(f"Failed to stop/pause playback {e}")
        else:
            return      #will implement playing random song from playlist

    def fetch_current_song(self):
        try:
            track = self.sp.current_user_playing_track(market=None, additional_types=('track',))
        except Exception as e:
            print(f"Errot: {e}")
            track = None

        if track is None or track['item'] is None:
            song_title = ''
            artist = ''
            album_cover_url=''
            self.album_cover_label.hide()       #maybe will set this to sth like "No media currently playing"? and set it to a nice green color 
        else:
            song_title = track['item']['name']
            artist = track['item']['artists'][0]['name']
            album_cover_url = track['item']['album']['images'][1]['url']
            image = QImage()
            image.loadFromData(requests.get(album_cover_url).content)

            image_pixmap = QPixmap(image)

            rescaled_image = image_pixmap.scaled(
                image_pixmap.width()//2,
                image_pixmap.height()//2, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            )

            self.album_cover_label.setPixmap(rescaled_image)
            self.album_cover_label.show()
        self.song_title_label.setText(song_title)
        self.artist_label.setText(artist)
        

    #-----------------------------------------------------------
            
    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()