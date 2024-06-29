
# YouTube MP4 Converter

This script uses `pytube` to download YouTube video links in MP4 file format.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description
This Python script allows users to download YouTube videos as MP4 files. It lists available video streams and lets the user choose which stream to download.

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
   git clone <repository-url>
   cd <repository-directory>
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

