"""
Flask application for Emotion Detection API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_api():
    """
    API endpoint to analyze emotions from a given text.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    if not text_to_analyze:
        return "Invalid text! Please try again!."

    emotions = emotion_detector(text_to_analyze)

    if not emotions.get('dominant_emotion'):
        return "Invalid text! Please try again!."

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    return response_text

@app.route('/')
def landing_page():
    """
    Renders the landing page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
