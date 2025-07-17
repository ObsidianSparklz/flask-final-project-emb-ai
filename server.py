"""
This module provides a Flask web app server for the Emotion Dectector app.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
Gets the qp from the Watson URL, passes it to emotion_detector, and formats the result string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response_dict = emotion_detector(text_to_analyze)
    if response_dict is None:
        return "Invalid text! Please try again!"
    dominant_emotion = response_dict.pop('dominant_emotion', None)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    score_strings = []
    for emotion, score in response_dict.items():
        score_strings.append(f"'{emotion}': {score}")
        formatted_scores = ", ".join(score_strings)

    return (
        f"For the given statement, the system response is {formatted_scores}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index, or main page, for the app.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
