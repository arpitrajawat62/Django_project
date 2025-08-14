import os
from dotenv import load_dotenv # type: ignore
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi # type: ignore
import google.generativeai as palm # type: ignore

load_dotenv()

# Set OpenAI API key once globally
api_key = os.getenv("GOOGLE_API_KEY")  # Reads the key
palm.configure(api_key=api_key)

def extract_video_id(url):
    query = urlparse(url)
    if 'youtube.com' in query.netloc:
        video_id = parse_qs(query.query).get("v")
        return video_id[0] if video_id else None
    return None

def generate_transcript(video):
    try:
        video_id = extract_video_id(video.url)
        if not video_id:
            raise Exception("Invalid YouTube URL")
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([x['text'] for x in transcript_data])
        video.transcript = transcript
        video.save()
        return transcript, None
    except Exception as e:
        return None, str(e)

def generate_notes_from_transcript(transcript):
    from google.generativeai import GenerativeModel
    
    prompt = f"Summarize the following transcript into detailed notes:\n\n{transcript}"
    try:
        
        model = GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API Error: {e}"
       
