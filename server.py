from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json


app = Flask("Emotion detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def dominant_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    result = json.loads(result)
    dominant = max(result['emotionPredictions'][0]['emotion'], key=result['emotionPredictions'][0]['emotion'].get)
    output = result['emotionPredictions'][0]['emotion']
    output['dominant_emotion'] = dominant
    formatted_json = json.dumps(output)
    return formatted_json

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)