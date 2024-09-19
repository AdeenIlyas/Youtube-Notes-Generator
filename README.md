# Youtube Notes Generator

![Screenshot 2024-09-14 023029](https://github.com/user-attachments/assets/78d950c9-99e1-44cd-ba54-25081cf3e4ae)

YouTube Notes Generator is an AI-powered tool that allows users to input a YouTube video URL, automatically extract key points from the video, and save the summary as a notes file.
Features
Flask Application: Run the application locally as a Flask web app.
API Endpoints: Accepts video URLs via cURL commands, returning AI-generated notes.
Dockerized: Automatically installs dependencies, runs test cases, and builds Docker containers.
How to run the application:
1.git clone https://github.com/yourusername/YouTube-Notes-Generator.git
2.cd YouTube-Notes-Generator
3.python app.py

# Run using curl:

1. Open command prompt
2. curl -X POST -H "Content-Type: application/json" -d "{\"url\":\"<youtube_url>\"}" http://localhost:5000/api/generate_notes  
![Screenshot 2024-09-07 234816](https://github.com/user-attachments/assets/5ed18a03-3364-410b-af2a-349691a33516)

# Run using docker


![Screenshot 2024-09-19 192725](https://github.com/user-attachments/assets/9d1a83ef-de15-4233-b67f-fdc5d7a1fa67)

The docker image has been uploaded on dockerhub.
1.Start docker
2. Run the command docker pull adeen1234/flasktest-app
3. Run the command docker run -p 5000:5000 adeen1234/flasktest-app:latest

