from flask import Flask, render_template, request, send_file, jsonify
from crewai import Crew, Process
from agents import interpreter, writer
from tasks import research_task, write_task
from crewai_tools import YoutubeVideoSearchTool
import os
import shutil

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    notes_content = ""
    if request.method == 'POST':
        url = request.form.get('url')

        if url:
            notes_content = generate_notes_from_url(url)
            return render_template('index.html', url=url, notes_content=notes_content)
        else:
            return render_template('index.html', error="Enter a valid URL ⚠️")

    return render_template('index.html')

@app.route('/api/generate_notes', methods=['POST'])
def generate_notes():
    if request.is_json:
        data = request.get_json()
        url = data.get('url')
    else:
        return jsonify({"error": "Invalid request format"}), 400

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    notes_content = generate_notes_from_url(url)
    if notes_content:
        return jsonify({"notes": notes_content})
    else:
        return jsonify({"error": "Failed to generate notes"}), 500

def generate_notes_from_url(url):
    tool = YoutubeVideoSearchTool(youtube_video_url=url)
    interpreter.tools = [tool]
    writer.tools = [tool]
    research_task.tools = [tool]
    write_task.tools = [tool]

    crew = Crew(
        agents=[interpreter, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        memory=True,
        cache=False,
        max_rpm=100,
        share_crew=True
    )

    crew.kickoff()

    file_path = os.path.join('notes.md')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    

    return None

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
