from moviepy.editor import *
import requests
import io
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS 
import os
import sys
import textwrap
from mutagen.mp3 import MP3

text = sys.argv[1]
print(text)

# fetching images from Hugging Face (Token and URL)
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def save(input,filename):
    response = requests.post(API_URL, headers=headers, json={"inputs": input})
    image = Image.open(io.BytesIO(response.content))
    image.save(filename)

    
# Add text to image
def add_text_to_image(file, value):
    # Open the image file
    image = Image.open(file)
    # Create a new ImageDraw object
    draw = ImageDraw.Draw(image)
    # Define font size and font
    font_size = 30
    font = ImageFont.truetype('arial.ttf', font_size)
    # Get image dimensions
    width, height = image.size
    # Define text and background colors
    text_color = (255, 255, 255)  # White text
    background_color = (0, 0, 0)   # Black background
    # Calculate the position to start drawing text
    text_y = height - 20  # Place text 20 pixels above the bottom

    # Wrap text based on image width and font size
    wrapped_text = textwrap.fill(value, width=(width - 20) // (font_size // 2))  # Adjust width as needed

    # Calculate text height
    text_height = len(wrapped_text.split('\n')) * font_size  # Assuming font size is the line height

    # Draw black rectangle as background for the text
    draw.rectangle([(0, text_y - text_height), (width, height)], fill=background_color)

    # Add wrapped text to the image
    draw.multiline_text((10, text_y - text_height), wrapped_text, fill=text_color, font=font, spacing=10)

    # Save the modified image
    image.save(file)


# GENERATING VOICE (MP3 FILE)
def text2speech(text,filename):
    # The text that you want to convert to audio 
    # Language in which you want to convert 
    mytext = text
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named 
    # welcome 
    myobj.save(filename)
    print(f"Trying to access audio file: {filename}")
    audio=MP3(filename)
    return audio.info.length
   
def voiceover_func():
    video_clip = VideoFileClip("video/video-output1.mp4")
    # Load the audio clip for the voice-over
    voiceover_clip = AudioFileClip("video/voice1.mp3")
    # Set the audio of the video clip to be the voice-over audio
    video_clip=video_clip.set_audio(voiceover_clip)
    # Write the new video with the voice-over audio
    video_clip.write_videofile("video/output_video_with_voiceover1.mp4")


# GENERATE VIDEO (INTEGRATED WITH TEXT AND SPEECH OVERLAY)
def generate_video(textPrompt):
    s=textPrompt
    i=0
    clips=[]
    audio_clips=[]
    s=s.split('.')
    print(s)
    for i in range(0, len(s), 2):
        combined_statements = ""
        if i < len(s) - 1:
            combined_statements += s[i] + "." + s[i+1]
            print(combined_statements)
        else:
            combined_statements += s[i]
        if(combined_statements==''):
            print('Do Nothing')
        else:
            file=f'video/images/img_{i}.jpg'
            audio_file=f'video/audio/Newaudio_{i}.mp3'
            save(combined_statements,file)
            add_text_to_image(file,combined_statements)
            t=text2speech(combined_statements, audio_file)
            print(t)
            clip=ImageClip(file).set_duration(t)
            audio_clip = AudioFileClip(audio_file)
            clips.append(clip)
            audio_clips.append(audio_clip)

    final_audio = concatenate_audioclips(audio_clips)
    video_clip = concatenate_videoclips(clips, method='compose')
    # audioclip=AudioFileClip("welcome.mp3")
    final_audio.write_audiofile("video/voice1.mp3")
    # video_clip = video_clip.set_audio(final_audio)
    video_clip.write_videofile("video/video-output1.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")
    #video_clip.set_audio(audioclip)
    voiceover_func()

generate_video(text)



