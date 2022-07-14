import re

from ytmp.download import downloadlink as dl
from ytmp.parse import parse as p
import argparse

def download(av, linku):
 
    lc = re.findall(".+(list=.+)&?",linku)
    if len(lc)>=1:
        link = f"https://www.youtube.com/playlist?{lc[0]}"
        p(link, av)
    else:
        dl(linku, av)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", dest = "video", help="for mp4/video download", nargs = "*", default=["none"])
    parser.add_argument("-a", "--audio",dest ="audio", help="for mp3/audio download", nargs = "*", default=["none"])
    args = parser.parse_args();

    #audio
    for linku in args.audio:
        if(linku == 'none'):
            continue
        download(False,linku)
    #video
    for linku in args.video:
        if(linku == 'none'):
            continue
        download(True,linku)

if __name__ == "__main__":
    main()
