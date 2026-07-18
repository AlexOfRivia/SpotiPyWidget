# SpotiPyWidget

A lightweight desktop widget for controlling Spotify, built with **Python**, **PyQt6**, and **Spotipy**.

SpotiPyWidget gives you a small, compact window showing your currently playing track, album cover, and a progress slider, with quick controls for playback - without needing to open the full Spotify app.

## Features

- 🎵 Displays the currently playing track title, artist, and album artwork
- ⏯️ Play / pause, skip to next / previous track
- 📊 Progress slider showing playback position, with click-and-drag seeking
- 🖥️ Compact, fixed-size desktop widget (250x275) built with PyQt6
- 🔐 Authentication via Spotify OAuth (handled through Spotipy)
- 🔄 Auto-refreshes the current track every 3 seconds and the progress bar every second

> **Note:** Volume control and shuffle/repeat toggles are not implemented yet - contributions welcome!

## Requirements

- Python 3.9+
- A Spotify account (**Premium required** - playback control endpoints used by this app, such as play/pause/seek/skip, are Premium-only)
- A registered [Spotify Developer](https://developer.spotify.com/dashboard) application (Client ID & Client Secret)
- An active Spotify session on some device (the app controls existing playback, it does not start playback on a device with no active session)

### Python dependencies

- `spotipy`
- `PyQt6`
- `requests`
- `python-dotenv`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AlexOfRivia/SpotiPyWidget.git
   cd SpotiPyWidget
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create an application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Add the following Redirect URI to your app settings (must match exactly):
   ```
   http://127.0.0.1:9090
   ```
3. Create a `.env` file in the project root with your credentials:
   ```env
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   ```

The app requests the following Spotify scopes:
- `user-read-private`
- `user-modify-playback-state`
- `user-read-playback-state`

## Usage

Run the widget with:

```bash
python widget.py
```

On first launch, a browser window will open asking you to authorize the application with your Spotify account. After granting access, the widget will appear and start displaying your current playback.

## Project Structure

```
SpotiPyWidget/
├── widget.py                # Application entry point (UI + Spotify logic)
├── requirements.txt        # Python dependencies
├── .env                     # Your local credentials (not committed)
└── README.md
```

Currently the whole application, the PyQt6 `MainWindow` widget and the Spotipy integration - lives in a single `widget.py` file for simplicity. Splitting the UI and the Spotify client into separate modules is a natural next step as the project grows.

## Known Limitations / Roadmap

- API calls are currently made on the main thread, which can make the UI briefly unresponsive during network requests. Moving Spotify calls to a `QThread` is planned.
- No volume, shuffle, or repeat controls yet.
- No handling for the case where no active Spotify device/session exists.

## Built With

- [Python](https://www.python.org/)
- [PyQt6](https://pypi.org/project/PyQt6/) - desktop GUI framework
- [Spotipy](https://spotipy.readthedocs.io/) - lightweight Python client for the Spotify Web API

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/AlexOfRivia/SpotiPyWidget/issues) or open a pull request.

## Disclaimer

SpotiPyWidget is an independent, unofficial project and is not affiliated with, endorsed by, or sponsored by Spotify AB.
