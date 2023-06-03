import sponsorblock as sb
from sponsorblock import Segment
import os
import datetime
from moviepy.editor import VideoFileClip, concatenate_videoclips

client = sb.Client()


def get_segments(url: str) -> list[Segment]:
    try:
        return client.get_skip_segments(url)
    except Exception:
        pass


def sponsorblock(url, file="assets/video.mp4"):
    segments = get_segments(url)

    if segments is None:
        print("sponsorblock failed")
        return 1

    clips = []
    clip = VideoFileClip(file)
    start = 0
    for segment in segments:
        end = segment.start

        if segment.category in ["poi_hightlight", "filler", "interaction"]:
            continue
        try:
            clips.append(clip.subclip(start, end))
        except ValueError:
            pass

        start = segment.end

    if len(clips) == 1:
        return

    combined = concatenate_videoclips(clips)
    combined.write_videofile("assets/video_final.mp4")

    clip.close()

    os.remove("assets/video.mp4")
    os.rename("assets/video_final.mp4", file)
