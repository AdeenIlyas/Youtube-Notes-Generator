from crewai import Agent
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

interpreter = Agent(
    role='YouTube Video Analyst',
    goal='Analyze a YouTube video to identify its primary themes, key arguments, and supporting evidence. Provide a detailed breakdown of the content, including any relevant statistics, examples, or case studies.',
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned video analyst with expertise in dissecting complex content. Your goal is to delve deep into the provided YouTube video, extracting its core themes and supporting arguments. Employ your analytical skills to identify any relevant statistics, examples, or case studies that strengthen the video's points."
    ),
    tools=[],
    allow_delegation=True
)

writer = Agent(
    role='Concise Note-Taker',
    goal='Create a concise and informative summary of the key points from the video analysis. Focus on capturing the essence of the content in a clear and concise manner.',
    verbose=True,
    memory=True,
    backstory=(
        "As a skilled note-taker, your task is to distill the complex analysis provided by the YouTube Video Analyst into a concise and informative summary. Focus on capturing the most essential points and presenting them in a clear and easy-to-understand format."
    ),
    tools=[],
    allow_delegation=False
)