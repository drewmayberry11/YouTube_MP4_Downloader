
# YouTube MP4 Converter

## Downlaod videos from youtube for free in MP4 format. 

## Description
This Python script allows users to download YouTube videos as MP4 files. It lists available video streams and lets the user choose which stream to download.

It works with alot of other social media platforms like X and Instagram, but has some issues sometimes with other websites outside of YouTube.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features
- Download YouTube videos in MP4 format
- Lists available video streams with resolution and MIME type
- User-friendly command-line interface

## Dependencies
The script requires the following dependencies:
- `pytube`

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/drewmayberry11/YouTube_MP4_Downloader.git
   cd YouTube_to_MP4_Downloader
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```sh
   pip install pytube
   ```

## Usage
1. **Run the script:**
   ```sh
   python youTube_Mp4_Converter.py
   ```

2. **Follow the prompts:**
   - Enter the YouTube URL of the video you wish to download.
   - Enter the directory path where you want to save the downloaded video (leave blank for the current directory).
   - Choose the desired video stream from the list of available streams.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

