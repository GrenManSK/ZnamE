import contextlib
import sponsorblock as sb
from sponsorblock import Segment
import os
import datetime
from moviepy import VideoFileClip, concatenate_videoclips

client = sb.Client()


def get_segments(url: str) -> list[Segment]:
    """
    The get_segments function takes a url and returns the segments of that url.
        Args:
            url (str): The URL to get the segments from.
        Returns: 
            list[Segment]: A list of Segment objects representing each segment in the URL.
    
    :param url: str: Pass in the url of the video to be downloaded
    :return: A list of segment objects
    """
    with contextlib.suppress(Exception):
        return client.get_skip_segments(url)


def sponsorblock(url, file="assets/video.mp4"):
    """
    The sponsorblock function takes a url and an optional file name as arguments.
    The function then calls the get_segments function to retrieve the segments of 
    the video from the url. If no segments are returned, it prints &quot;sponsorblock failed&quot;
    and returns 1. Otherwise, it creates a list of clips that will be concatenated into 
    a new video without sponsor blocks or filler content (poi_highlight, filler and interaction). 
    It does this by creating VideoFileClip objects for each segment in the original video that is not one of these categories. It then concatenates all these clips together
    
    :param url: Get the segments from the sponsorblock api
    :param file: Specify the file to be edited
    :return: A video file with the sponsor block removed
    """
    segments = get_segments(url)

    if segments is None:
        print("sponsorblock failed")
        return 1

    clips = []
    clip = VideoFileClip(file)
    start = 0
    for segment in segments:
        end = segment.start

        if segment.category in ["poi_highlight", "filler", "interaction"]:
            continue
        with contextlib.suppress(ValueError):
            clips.append(clip.subclip(start, end))
        start = segment.end

    if len(clips) == 1:
        return

    combined = concatenate_videoclips(clips)
    combined.write_videofile("assets/video_final.mp4")

    clip.close()

    os.remove("assets/video.mp4")
    os.rename("assets/video_final.mp4", file)
