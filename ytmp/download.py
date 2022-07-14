import subprocess as pr
import yt_dlp as yd
import getpass
import os
def downloadlink(vid, av, isplaylist = False, playlistname = "music/"):
	video_info = yd.YoutubeDL().extract_info(
		url = vid,download=False
	)
	m34 = "mp4" if av else "mp3"
	filename = f"{video_info['title']}.{m34}"
	for ind,let in enumerate(filename,0):
		if let == "/" or let == "|" or let == ":" or let == "?":
			filename = filename[:ind] + filename[ind+1:]
	if isplaylist is True:
		filename = playlistname + filename
	filename = f"{os.path.expanduser('~')}/Music/{filename}"
	if not av: 
	    options={
	        'format':'bestaudio/best',
	        'keepvideo':False,
	        'outtmpl':filename
	    }
	else:
	    options={
	        'format':'bestvideo+bestaudio/best',
	        'outtmpl':filename,
	    }
	
	with yd.YoutubeDL(options) as ydl:
	 ydl.download([video_info['webpage_url']])

