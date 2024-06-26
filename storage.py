# storing videos in storage(Firebase)
import firebase_admin
from firebase_admin import credentials, storage
import sys
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
storage_bucket = os.getenv('FIREBASE_STORAGE_BUCKET')

email = sys.argv[1]
title = sys.argv[2]
print("Email received in storage.py:",email)
    # Initialize Firebase Admin SDK
cred = credentials.Certificate(os.getenv("account_key"))  # Replace with your service account key file
firebase_admin.initialize_app(cred, {
    'storageBucket': storage_bucket  # Replace with your storage bucket name
})

    # Get a reference to the storage service
bucket = storage.bucket()

    # Upload a local file to the bucket
blob = bucket.blob(f"{email}/{title}.mp4")
blob.upload_from_filename("video/output_video_with_voiceover1.mp4")

print("File uploaded successfully!")
