from ytmp.download import downloadlink
import pytube
def parse(url,av):
    yt = pytube.Playlist(f'{url}')
    name,newlist = yt.title, yt.video_urls
    name += "/"
    for ind,vid in enumerate(newlist,1):
        print(f"downloading link {ind}/{len(newlist)}")
        try:
            downloadlink(vid ,av ,True ,name)
        except:
            continue
