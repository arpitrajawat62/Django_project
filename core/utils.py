from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    from urllib.parse import urlparse, parse_qs
    query = urlparse(url)
    if 'youtube.com' in query.netloc:
        video_id = parse_qs(query.query).get("v")
        return video_id[0] if video_id else None
    elif 'youtu.be' in query.netloc:
        return query.path.lstrip('/')
    return None

def generate_transcript(video):
    try:
        video_id = extract_video_id(video.url)
        if not video_id:
            raise Exception("Invalid YouTube URL")
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([x['text'] for x in transcript_data])
        video.transcript = transcript
        video.error_message = ""
    except Exception as e:
        video.error_message = str(e)
    video.save()


