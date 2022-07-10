import re 

from download import downloadlink as dl
from parse import parse as p
import argparse

def download(av, linku):
    if linku == "none": 
        return
    lc = re.findall(".+(list=.+)&?",linku)
    if len(lc)>=1:
        link = f"https://www.youtube.com/playlist?{lc[0]}"
        p(link, av)
    else:
        dl(linku, av)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-v", "--video", dest = "video", help="for mp4/video download", nargs = "*", default="none")
    parser.add_argument("-a", "--audio",dest ="audio", help="for mp3/audio download", nargs = "*", default="none")
    args = parser.parse_args();

    
    #audio
    for linku in args.audio:
        download(False,linku)
    #video
    for linku in args.video:
        download(True,args.video)
