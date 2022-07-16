from ytmp.download import downloadlink
import pytube
import subprocess as sp
def parse(url,av):
    try:
        yt = pytube.Playlist(f'{url}')
        name,newlist = yt.title, yt.video_urls
        name += "/"
        for ind,vid in enumerate(newlist,1):
            print(f"downloading link {ind}/{len(newlist)}")
            try:
                downloadlink(vid ,av ,True ,name)
            except:
                continue

    except:
        sp.run(["gxmessage", "please make sure that the playlist is not private"])
