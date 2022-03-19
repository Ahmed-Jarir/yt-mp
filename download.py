import subprocess as pr
import youtube_dl
import getpass
import os
def downloadlink(vid, av, isplaylist = False, playlistname = "music/"):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = vid,download=False
    )
    m34 = "mp4" if av else "mp3"
    filename = f"{video_info['title']}.{m34}"
    for ind,let in enumerate(filename,0):
        if let == "/":
            filename = filename[:ind] + filename[ind+1:]
    if isplaylist is True:
        filename = playlistname + filename
    filename = f"{os.path.expanduser('~')}/Music/{filename}"
    if not av: 
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
            'cookiefile': 'cookies.txt',
        }
    else:
        options={

            'format':'bestvideo+bestaudio/best',
            'outtmpl':filename,
        }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

