import imageio_ffmpeg as ffmpeg
import yt_dlp


def download_youtube_video(url, output_path='.', audio_only=False) -> str:
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg.get_ffmpeg_exe()
    }

    if audio_only:
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)
            print(result['title'])
            return result['title']
    except Exception as e:
        print(f"Error during download: {e}")
        return None