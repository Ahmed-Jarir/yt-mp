import sys
import re 

from download import downloadlink as dl
from help import help
from parse import parse as p

def download(av, linku):
    lc = re.findall(".+(list=\w+)&?",linku)
    if len(lc)>=1:
        link = f"https://www.youtube.com/playlist?{lc[0]}"
        p(link, av)
    else:
        link = linku
        dl(link, av)


if __name__ == "__main__":
#    try:
    arg = sys.argv
    if arg[1] == "-h":
        help()
    else:
        av = True if arg[1]=="-v" else False

        if len(arg) <= 3:
            download(av,arg[2])
        else :
            for linku in arg[2:]:
                download(av,linku)
                

#    except:
#        print("not enough arguments\nif you need help please use the following command \"ytmp -h\"\nand please make sure the playlist or video that you're trying to download is public or unlisted")
