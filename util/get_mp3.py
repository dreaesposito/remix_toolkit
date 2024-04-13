import os.path
from pytube import YouTube

from util import get_key_tempo

""" =================================================
This method uses the specified path and URL input from
the user download and save the .flac audio file 
============================================= """


def create(link, path, get_info):
    # url input from user
    yt = YouTube(link)

    # extract audio only
    video = yt.streams.filter(only_audio=True).first()

    # set path as user input
    destination = path
    result = 'Saved to directory: ' + destination + '\n'

    # download
    out_file = video.download(output_path=destination)

    # save
    base, ext = os.path.splitext(out_file)

    # rename folder path
    base = base.replace('\\', '/')
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    song_path = new_file
    result += yt.title + ' has been successfully downloaded!'

    if get_info:  # get BPM and key
        result += get_key_tempo.get_bpm(song_path)
        result += get_key_tempo.get_key_signature(song_path)

    # return result message
    return result

