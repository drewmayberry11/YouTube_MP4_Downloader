
#!/usr/bin/env python3
# youtube_mp4_downloader.py

"""
Author: Drew Mayberry
Date: June 28, 2024
Description: This script Uses yt-dlp to download youtube video links to MP4 file format.
Version: 1.0
"""
from pytube import YouTube
import os


def list_available_streams(yt):
    """
    Lists available streams for a given YouTube video.

    Parameters:
    yt (YouTube): YouTube object representing the video.

    Returns:
    dict: Dictionary of available streams with indices as keys.
    """
    streams = yt.streams.filter(progressive=True, file_extension='mp4')
    available_streams = {i: stream for i,
                         stream in enumerate(streams, start=1)}
    for i, stream in available_streams.items():
        print(f"{i}: {stream.resolution}, {stream.mime_type}")
    return available_streams


def download_video(stream, path):
    """
    Downloads a selected stream to the specified path.

    Parameters:
    stream (Stream): The stream to be downloaded.
    path (str): The directory path where the file will be saved.
    """
    try:
        stream.download(output_path=path)
        print(f"Download completed! File saved in {path}")
    except Exception as e:
        print(f"Error during download: {e}")


def main():
    """
    Main function to drive the script. Prompts the user for YouTube URL and download directory,
    lists available streams, and downloads the selected stream.
    """
    url = input("Enter the YouTube URL: ")
    path = input(
        "Enter the download directory path (leave blank for current directory): ")
    path = path or "."

    try:
        yt = YouTube(url, on_progress_callback=lambda stream, chunk,
                     bytes_remaining: print("Downloading...", end="\r"))
        print(f"Video Title: {yt.title}\nAvailable streams:")
        available_streams = list_available_streams(yt)

        choice = int(
            input("Enter the number of the stream you want to download: "))
        if choice in available_streams:
            download_video(available_streams[choice], path)
        else:
            print("Invalid choice. Please restart the program.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
