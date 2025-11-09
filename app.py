import streamlit as st
import os
from src.youtube_summarizer import YouTubeVideoSummarizer
from src.youtube_summarizer.utils import extract_video_id

st.set_page_config(
    page_title="YouTube Video Transcriber",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube Video Transcriber")
st.markdown("Convert YouTube videos to text using AI-powered transcription")

st.markdown("---")

api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found in environment variables!")
    st.info("""
    To use this app, you need to add your Google Gemini API key:
    
    1. Get a free API key from: https://aistudio.google.com/apikey
    2. Add it to your Replit Secrets as `GEMINI_API_KEY`
    3. Restart the application
    """)
    st.stop()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Enter YouTube Video")
    
    url_input = st.text_input(
        "YouTube URL or Video ID",
        placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ or dQw4w9WgXcQ",
        help="Paste a YouTube URL or just the video ID"
    )
    
    transcribe_button = st.button("🎙️ Transcribe Video", type="primary", use_container_width=True)

with col2:
    st.subheader("ℹ️ How to Use")
    st.markdown("""
    1. Paste a YouTube URL
    2. Click "Transcribe Video"
    3. Wait for processing
    4. Get your transcript!
    
    **Supported formats:**
    - `youtube.com/watch?v=...`
    - `youtu.be/...`
    - Direct video ID
    """)

st.markdown("---")

if transcribe_button and url_input:
    try:
        video_id = extract_video_id(url_input)
        
        st.success(f"✅ Video ID detected: `{video_id}`")
        
        progress_container = st.container()
        
        with progress_container:
            with st.spinner("🎵 Downloading audio from YouTube..."):
                summarizer = YouTubeVideoSummarizer()
                audio_path = summarizer.download_audio(video_id)
            
            st.success(f"✅ Audio downloaded: `{os.path.basename(audio_path)}`")
            
            with st.spinner("📝 Transcribing audio with Google Gemini AI..."):
                transcript = summarizer.transcribe_audio(audio_path)
            
            st.success("✅ Transcription completed!")
        
        st.markdown("---")
        st.subheader("📄 Transcription Result")
        
        col_a, col_b = st.columns([3, 1])
        
        with col_a:
            st.info(f"**Video ID:** {video_id}")
        
        with col_b:
            st.metric("Characters", len(transcript))
        
        transcript_area = st.text_area(
            "Full Transcript",
            value=transcript,
            height=400,
            help="You can copy this text or download it below"
        )
        
        col_download1, col_download2 = st.columns(2)
        
        with col_download1:
            st.download_button(
                label="💾 Download as TXT",
                data=transcript,
                file_name=f"{video_id}_transcript.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col_download2:
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.code(transcript, language=None)
                st.success("✅ Transcript displayed above - use your browser's copy function")
        
        st.markdown("---")
        st.subheader("🎬 Video Preview")
        st.video(f"https://www.youtube.com/watch?v={video_id}")
        
    except ValueError as e:
        st.error(f"❌ Invalid URL: {str(e)}")
        st.info("Please enter a valid YouTube URL or video ID")
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.info("Please try again or check if the video is accessible")

elif transcribe_button:
    st.warning("⚠️ Please enter a YouTube URL or video ID first")

st.markdown("---")

with st.expander("📚 Example Videos to Try"):
    st.markdown("""
    Try these example video IDs:
    - `dQw4w9WgXcQ` - Popular music video
    - `jNQXAC9IVRw` - "Me at the zoo" (first YouTube video)
    - Any YouTube URL you want to transcribe!
    
    **Note:** Processing time depends on video length. Shorter videos process faster.
    """)

with st.expander("🔧 Technical Details"):
    st.markdown("""
    **How it works:**
    1. Extracts video ID from URL
    2. Downloads audio using yt-dlp
    3. Converts to MP3 format
    4. Uploads to Google Gemini
    5. AI transcribes the audio
    6. Returns text transcript
    
    **Technologies:**
    - **yt-dlp**: YouTube audio extraction
    - **Google Gemini AI**: Audio transcription
    - **Streamlit**: Web interface
    - **FFmpeg**: Audio processing
    """)

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Made with ❤️ using Streamlit and Google Gemini AI</div>",
    unsafe_allow_html=True
)
