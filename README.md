# Youtube Notes Generator

![Screenshot 2024-09-14 023029](https://github.com/user-attachments/assets/78d950c9-99e1-44cd-ba54-25081cf3e4ae)

YouTube Notes Generator is an AI-powered tool that allows users to input a YouTube video URL, automatically extract key points from the video, and save the summary as a notes file.

# Features

Real-Time Transcription: Analyzes and transcribes YouTube videos in real time.

Key Insights Extraction: Automatically extracts key points and insights from the video content.

Concise Notes Generation: Creates short, concise notes based on the extracted insights.

Notes File Storage: Saves the generated notes in a file for easy access and reference.


# How to run the application:

1.git clone https://github.com/AdeenIlyas/YouTube-Notes-Generator.git

2. pip install -r requirements.txt

3.cd YouTube-Notes-Generator

4.python app.py

# Run using curl:

1. Run python app.py (to run server)

2. Open command prompt

3. curl -X POST -H "Content-Type: application/json" -d "{\"url\":\"<youtube_url>\"}" http://localhost:5000/api/generate_notes  
![Screenshot 2024-09-07 234816](https://github.com/user-attachments/assets/5ed18a03-3364-410b-af2a-349691a33516)

# Run using docker


![Screenshot 2024-09-19 192725](https://github.com/user-attachments/assets/9d1a83ef-de15-4233-b67f-fdc5d7a1fa67)

The docker image has been uploaded on dockerhub which automatically installs dependencies, runs test cases, and builds Docker containers.


1. Start docker


2. Run the command docker pull adeen1234/flasktest-app


3. Run the command docker run -p 5000:5000 adeen1234/flasktest-app:latest

