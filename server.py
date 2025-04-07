"""server flask module to handle emotions"""
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/")
def render_index_page():
    """route home - render the html page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def dominant_emotion():
    """
    Detects the dominant emotion in the input text from the query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    print(result)
    if result["dominant_emotion"] is None:
        return "Invalid input! Try again."

    emotion = result['emotionPredictions'][0]['emotion']
    dominant = max(emotion, key=emotion.get)
    output = result['emotionPredictions'][0]['emotion']
    output['dominant_emotion'] = dominant
    formatted_json = json.dumps(output)
    return formatted_json

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
