<div align="center">

# ▶️ YT Playlist Importer

**Recreate a YouTube playlist from a Google Takeout CSV using the YouTube Data API.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![YouTube API](https://img.shields.io/badge/YouTube_Data_API_v3-FF0000?style=flat-square&logo=youtube&logoColor=white)
![OAuth 2.0](https://img.shields.io/badge/OAuth_2.0-4285F4?style=flat-square&logo=google&logoColor=white)

</div>

## Why

Google Takeout exports your playlists as CSV files of video IDs, but there's no button to import them back — into the same account after a cleanup, or into a different one. This script does it.

## What it does

1. Signs you in with Google OAuth (opens a browser window).
2. Reads a Takeout playlist CSV.
3. Creates a new **private** playlist named after the CSV file.
4. Skips videos that have been deleted or made unavailable.
5. Adds every remaining video to the new playlist.

## Setup

1. In the [Google Cloud Console](https://console.cloud.google.com/), create a project, enable **YouTube Data API v3**, and create an **OAuth client ID** of type *Desktop app*.
2. Download the credentials and save them next to `main.py` as `client_secret.json`.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
# Enter the takeout csv playlist: path/to/My Playlist.csv
```

> Each insert costs YouTube API quota (50 units). The default daily quota of 10,000 units covers roughly 200 videos a day.

## Author

**Muhammed Safar** — [@safar-byte](https://github.com/safar-byte)
