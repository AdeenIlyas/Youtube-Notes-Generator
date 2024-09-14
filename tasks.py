from crewai import Task
from agents import interpreter, writer

research_task = Task(
    description=(
        "**Step 1: Watch the video.**  Pay close attention to the speaker's points and visuals.\n"
        "**Step 2: Identify key topics and insights.**  Focus on the main ideas and takeaways from the video.\n"
        "**Step 3: Generate a comprehensive report.**  Summarize the key topics and insights in a clear and concise manner.\n"
        "**Example Output:** A report titled 'Key Takeaways from [Video Title]' outlining the main points discussed in the video."
    ),
    expected_output='A comprehensive report highlighting the main topics and key insights from the video.',
    tools=[],
    agent=interpreter,
)

write_task = Task(
    description=(
        "**Step 1: Access the output from the 'research_task'.**  This will provide information on key topics and insights from the video.\n"
        "**Step 2: Summarize the key points.**  Extract the most important information from the 'research_task' output.\n"
        "**Step 3: Generate concise notes.**  Create short and easy-to-understand notes that capture the essence of the video.\n"
        "**Example Output:** A file named 'notes.md' containing bullet points or short paragraphs summarizing the key points from the video."
    ),
    expected_output='Summarized notes explaining the key points and topics from the video content.',
    tools=[],
    agent=writer,
    async_execution=False,
    output_file='notes.md'
)