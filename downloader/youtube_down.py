from pytube import YouTube
import os


def download_fail():
    return {'status': False, 'error': 'because of copyright policy youtube blocked download'}

def img_to_base64(img_url):
    pass

def download(url, mode):
    current_path = os.path.dirname(__file__)
    try:
        video = YouTube(url)
    except KeyError as e:
        print(str(e))
        return download_fail()
    streams = video.streams
    video_title = video.title
    video_thumbnail_url = video.thumbnail_url
    video_len = video.length
    if mode == 'video':
        # mp4 download only
        download_path = 'video'
        stream = streams.filter(file_extension='mp4', res='1080p')[-1]
        if stream == 0:
            stream = streams.filter(file_extension='mp4', res='720p')[-1]
            if stream == 0:
                print('fail')
                return download_fail()
    else:
        # mode == 'audio'
        download_path = 'audio'
        stream = streams.filter(only_audio=True)[0]
    
    file_path = os.path.join(current_path, download_path)
    stream.download(file_path)
    return {
        'status': True,
        'title': video_title,
        'thumbnail': video_thumbnail_url,
        'length': video_len,
        'path': file_path
    }

if __name__ == "__main__":
    download('https://www.youtube.com/watch?v=mH0_XpSHkZo', 'video')

# https://www.youtube.com/watch?v=P-eJI00efng
# https://www.youtube.com/watch?v=mH0_XpSHkZo
