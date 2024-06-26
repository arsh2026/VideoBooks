# fetching videos from database (firebase)
import firebase_admin
from firebase_admin import credentials, storage
import webbrowser
from uuid import uuid4
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
storage_bucket = os.getenv('FIREBASE_STORAGE_BUCKET')
# Initialize Firebase Admin SDK
cred = credentials.Certificate(os.getenv("account_key"))  # Replace with your service account key file
firebase_admin.initialize_app(cred, {
'storageBucket': storage_bucket  # Replace with your storage bucket name
})

# Generate a URL for the video file with an access token
def generate_video_url(blob):
    # Generate a unique token (e.g., UUID)
    access_token = str(uuid4())

    # Set token expiration time (e.g., 1 hour)
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    # Construct the signed URL with the access token
    signed_url = blob.generate_signed_url(expiration=expiration_time, version="v4", access_token=access_token)

    return signed_url


def FetchVideo(email,title):
    # Get a reference to the storage service
    bucket = storage.bucket()
   
    # Get a reference to the video file
    blob = bucket.blob(f"{email}/{title}.mp4")
    # Get the signed URL with access token
    video_url = generate_video_url(blob)
    return video_url

# Open the video URL in a new tab
# webbrowser.open_new_tab(video_url)