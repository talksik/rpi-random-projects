from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, abort, send_file
from tempfile import NamedTemporaryFile
import tts
import whisper

# Load the Whisper model:
model = whisper.load_model("base")

app = Flask(__name__)


@app.route("/")
def helloWorld():
    return "Hello, World!"


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400, "No files submitted!")

    # For each file, let's store the results in a list of dictionaries.
    results = []

    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(temp)
        # Let's get the transcript of the temporary file.
        result = model.transcribe(temp.name)
        # Now we can store the result object for this file.
        results.append(
            {
                "filename": filename,
                "transcript": result["text"],
            }
        )

    # This will be automatically converted to JSON.
    return {"results": results}


# endpoint to convert text to speech and return the file
@app.route("/tts", methods=["POST"])
def text_to_speech():
    # get the text from the request json
    content = request.get_json()
    text = content['text']
    
    if not text:
        abort(400, "Please provide text to convert to speech!")

    # call the text_to_wav function from tts.py
    fileName = tts.text_to_wav(
        voice_name="en-GB-Neural2-B",
        text=text,
    )

    # return the file
    return send_file(f"{fileName}", mimetype="audio/wav")


if __name__ == "__main__":
    # 0.0.0.0 opens up to all ipv4 addresses
    app.run(host="0.0.0.0", port=5001, debug=True)
