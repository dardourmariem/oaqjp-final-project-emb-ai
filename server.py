from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def get_dominant_emotion(text):
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    result['dominantEmotion'] =max(result['emotionPredictions'][0]['emotion'], key=result['emotionPredictions'][0]['emotion'].get)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)